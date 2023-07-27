from typing import Optional

class Controller:
    name: str
    children: list["Controller"]
    header: Optional["Controller"]

    def __init__(self, name: str) -> None:
        self.name = name
        self.children = []
        self.header = None
    
    def add_child(self, child: "Controller"):
        if self._is_repeat__(child):
            child = self._generate_repeat_new_child__(child)
        self.children.append(child)
        child.header = self

        return child
        
    def remove_child(self, child: "Controller"):
        self.children.remove(child)
    
    def to_did_str(self) -> str:
        """
        Return a string of controllers from the header to the current controller
        """
        did_list = self.__to_did_list__()
        return "/".join([controller.name for controller in did_list])

    def __to_did_list__(self) -> list["Controller"]:
        """
        Return a list of controllers from the header to the current controller
        """
        if self.header is None:
            return [self]
        return [self] + self.header.__to_did_list__()
        
    def _is_repeat__(self, new_child: "Controller") -> bool:
        """
        Check if the new child is already in the children list
        """
        return new_child in self.children

    def _generate_repeat_new_child__(self, new_child: "Controller") -> "Controller":
        """
        Add number to the end of the new child name
        """
        new_name = f"{new_child.name}{len(self.children)}"
        return Controller(new_name) 
        
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Controller):
            return self.name == __value.name
        return False
