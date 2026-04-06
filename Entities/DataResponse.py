from typing import TypeVar, Generic, List, Optional, Any

T = TypeVar('T')

class DataResponse(Generic[T]):
    def __init__(self, item : Optional[T] = None, items : List[T] = [], db : Any = None, IsSuccess=True):
        if db:
            self.IsSuccess : bool = getattr(db, 'retIsSuccess', IsSuccess)
            self.Message : str = getattr(db, 'retMessage', "")
            self.count : int = getattr(db, 'retCount', 0)
            self.item = item
            self.items = items

        else:
            self.IsSuccess = IsSuccess
            self.Message = ""
            self.count = 0
            self.item = None
            self.items = None