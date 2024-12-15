from collections import OrderedDict
from datetime import datetime 
from pydantic import BaseModel, ConfigDict

class Event(BaseModel):

    model_config = ConfigDict(frozen=True)
    event_a :str = "aaa"

    def cus_serialize(self) -> dict:
        return OrderedDict(self.__dict__)

class UserContext(BaseModel):

    model_config = ConfigDict(frozen=True)
    weekday: int = datetime.now().weekday()
    events: Event

    def cus_serialize(self) -> dict:

        result = {
                key: 
                    (
                        self.__dict__[key].cus_serialize()
                        if hasattr(self.__dict__[key], 'serialize')
                        else self.__dict__[key]
                    )
                for key in OrderedDict(self.__dict__)
        }

        return result

def main():
    user_events = Event(event_a = 'ssss')
    user_context = UserContext(events = user_events)

if __name__ == "__main__":
    main()

