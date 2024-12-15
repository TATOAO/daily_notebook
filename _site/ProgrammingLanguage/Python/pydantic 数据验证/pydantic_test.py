


class User(BaseModel):
    id: int
    name: str
    # signup_ts: datetime | None
    friends: list[int] | None


external_data = {
        "id" : 2032,
        "name": 'alan',
        "friends": None,
        }

user = User(**external_data)
