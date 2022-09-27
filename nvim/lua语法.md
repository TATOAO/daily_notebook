
# Lua 语法

https://github.com/nanotee/nvim-lua-guide

https://learnxinyminutes.com/docs/lua/

## bool

``` lua



-- Undefined variables return nil.
-- This is not an error:
foo = anUnknownVariable  -- Now foo = nil.

aBoolValue = false

-- Only nil and false are falsy; 0 and '' are true!
if not aBoolValue then print('it was false') end

-- 'or' and 'and' are short-circuited.
-- This is similar to the a?b:c operator in C/js:
ans = aBoolValue and 'yes' or 'no'  --> 'no'

```


## for loop

``` lua


karlSum = 0
for i = 1, 100 do  -- The range includes both ends.
  karlSum = karlSum + i
end

-- Use "100, 1, -1" as the range to count down:
fredSum = 0
for j = 100, 1, -1 do fredSum = fredSum + j end

-- In general, the range is begin, end[, step].

```


## 