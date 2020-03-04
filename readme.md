<h1 align="center">
    🧽 SpOnGeCaSqL
</h1>
<h2 align="center">
    (spongecaSQL)
</h2>
<p align="center">
    <img src="https://github.com/the-new-sky/spongecaSQL/raw/master/spongebob.jpg" alt="Mocking Spongebob meme">
</p>

**SQL** is great but it is not *case-sensistive*. Which means that keywords and objects can be called in UPPERCASE or in <sub>lowercase</sub>.

That's bad. It doesn't discourage consistency since some developer will write `SELECT`, `select` or even `Select`.

Here is a standard to fix this issue : **🧽 SpOnGeCasE**.

# Usage

```sh
$ python3 spongecasql.py yourfile.sql
```

### Before

```sql
/*
    Comments are ignored
*/
# Those too
-- Those too
SELECT *  
FROM Customer
WHERE country = 'US'
AND city = 'New-York City'
```

### After

```sql
/*
    Comments are ignored
*/
# Those too
-- Those too
sElEcT *  
FrOm cUsToMeR
WhErE CoUnTrY = 'US'
AnD CiTy = 'New-York City'
```
