Great question! You're right that `@property` **alone** gives you the ability to define computed attributes in normal Python classes. However, in **Pydantic v2**, `@computed_field` serves an important additional purpose beyond just Python behavior.

---

### ✅ The Difference: Why `@computed_field` is Needed in Pydantic v2

#### If you only use `@property`:

```python
class Rectangle(BaseModel):
    width: int
    length: int

    @property
    def area(self) -> int:
        return self.width * self.length
```

* ✅ You **can access** `area` via `r.area`.
* ❌ But `area` will **not be included in `.model_dump()` or `.dict()` or `.json()` output**.
* ❌ It will **not be part of the schema**, so tools like OpenAPI or JSON Schema won't see it.

---

#### If you add `@computed_field`:

```python
from pydantic import BaseModel, computed_field

class Rectangle(BaseModel):
    width: int
    length: int

    @computed_field
    @property
    def area(self) -> int:
        return self.width * self.length
```

* ✅ `area` is still a computed `@property`.
* ✅ It **is included in `.model_dump()` and `.model_json()`**.
* ✅ It shows up in the schema (e.g., OpenAPI or JSON Schema).
* ✅ Useful for FastAPI responses and documentation.

---

### 📌 Summary

| Feature                        | `@property` Only | `@property + @computed_field` |
| ------------------------------ | ---------------- | ----------------------------- |
| Usable at runtime              | ✅                | ✅                             |
| Included in `.model_dump()`    | ❌                | ✅                             |
| Included in OpenAPI/Schema     | ❌                | ✅                             |
| Declares computed field intent | ❌                | ✅                             |

---

### 🧠 When to use `@computed_field`

Use `@computed_field` when:

* You want the computed value to **appear in serialization**.
* You want tools like **FastAPI to include it in OpenAPI docs**.
* You want to explicitly signal this field is computed (for maintainability and introspection).

If you only need the value at runtime and don't care about serialization, `@property` is enough.

Let me know if you'd like to see what happens with `model_dump()` with and without it!

