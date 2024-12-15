
# yaml

```python
import yaml
with open('test.yml', 'r') as file:
   prime_service = yaml.safe_load(file)

print(prime_service)
```

rest:
  url: "https://example.org/primenumbers/v1"
  port: 8443
  b: true
  c: True
  d: "True"

