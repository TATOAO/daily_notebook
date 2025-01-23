
Handling NAT Traversal:
If peers are behind NAT (Network Address Translation) (common for home users or in some mobile networks), they may not have public IPs. For this, you can use STUN (Session Traversal Utilities for NAT) or TURN (Traversal Using Relays around NAT) protocols, or a service like ngrok to expose the local peer to the internet.

STUN (Session Traversal Utilities for NAT)



TURN (Traversal Using Relays around NAT)


NAT Types
Understanding NAT types is essential when working with STUN and TURN. There are different types of NAT that affect how peers communicate:

1. Full Cone NAT: STUN works well in this case because the peer can be reached directly using its public IP and port.
2. Restricted Cone NAT: STUN may still work, but only if the peer has previously communicated with the external IP/port.
3. Port Restricted Cone NAT: Similar to Restricted Cone NAT, but with stricter rules.
4. Symmetric NAT: This is the most restrictive type, and STUN does not work well with symmetric NAT. In this case, you need to use TURN.



WebRTC (Web Real-Time Communications) 是一项实时通讯技术，它允许网络应用或者站点，在不借助中间媒介的情况下，建立浏览器之间点对点（Peer-to-Peer）的连接



ICE 
ICE的全称Interactive Connectivity Establishment（互动式连接建立），由IETF的MMUSIC工作组开发出来的，它所提供的是一种框架，使各种NAT穿透技术可以实现统一。


https://www.cnblogs.com/ssyfj/p/14799326.html
