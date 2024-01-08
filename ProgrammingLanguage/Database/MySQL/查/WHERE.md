
## Query more

#### Like

有点像正则, 
% any characters,
_ one character.

```sql
SELECT *
FROM client
WHERE client_name LIKE '%LLC';

..
WHERE birth+date LIKE '____-10%';

```

