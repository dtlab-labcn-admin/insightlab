import json
from dotmap import DotMap
from enum import Enum


class objectTypeAttribute(Enum):
    """
    Enum to hold objectTypeAttribute.
    Ref: https://documentation.mindville.com/display/INSCLOUD/REST+API+-+Object+type+attributes
    """

    def __str__(self):
        return str(self.value)

    Default = 0
    Object = 1
    User = 2
    Confluence = 3
    Group = 4
    Status = 7


class objectDefaultTypeAttribute(Enum):
    """
    Enum to hold the default types
    """

    def __str__(self):
        return str(self.value)

    Text = 0
    Integer = 1
    Boolean = 2
    Double = 3
    Date = 4
    Time = 5
    DateTime = 6
    URL = 7
    Email = 8
    Textarea = 9
    Select = 10
    IPAddress = 11


class IQLResponse:
    """
    IQL Response object

    Args:
        raw_json (str): The raw response

    Attributes:
        parsed (DotMap): The response in a DotMap format
        iql (str): The original IQL query
        objects (str[]): Parsed objects
    """

    def __init__(self, raw_json):
        self.raw = raw_json
        self.parsed = DotMap(raw_json)
        self.iql = self.parsed.iql
        self.objects = self.parsed.objectEntries


class Attributes:
    """
    Structured object to hold attributes

    Args:
        object_type_attribute_id (str):  The attribute type's id.

    Attributes:
        objectAttributeValues (str): The values for the attribute
    """

    def __init__(self, object_type_attribute_id):
        self.objectTypeAttributeId = object_type_attribute_id
        self.objectAttributeValues = []

    def add_value(self, value):
        """
        Adds a value to an attribute

        Args:
            value (str): The value of the attribute
        """
        self.objectAttributeValues.append({"value": value})
    
    def add_values(self, values):
        """
        Adds values to an attribute

        Args:
            value (list): The values of the attribute
        """        
        for v in values:
            self.objectAttributeValues.append({"value": v})


class NewObject:
    """
    Base class for new object creation

    Args:
        object_type_id (str): The object type id to create

    Attributes:
        attributes (Attribute): The attributes of the object
    """

    def __init__(self, object_type_id):
        self.objectTypeId = object_type_id
        self.attributes = []

    def add_attribute(self, object_type_attribute_id, value):
        """
        Adds an attribute object to the newly created object.

        Args:
            object_type_attribute_id (str): The attribute type's id.
            value (str): The value of the attribute
        """
        a = Attributes(object_type_attribute_id)
        if isinstance(value, list):
            a.add_values(value)
        else:
            a.add_value(value)
        self.attributes.append(a)

class Object:
    """
    Base class for returning objects.

    Args:
        raw_json (str): The raw json data of the object

    Attributes:
        parsed (DotMap): The object parsed in a map
        id (str): The id of the object
        name (str): The name of the object
        objectKey (str): The key of the object
        objectSchema: The schema the object belongs to
        created (str): The object's creation timestamp
        updated (str): The object's last update timestamp
        hasAvatar (bool): If the object has an avatar
        attributes (DotMap[]): The attributes of the object
    """

    def __init__(self, raw_json):
        self.raw = raw_json
        self.parsed = DotMap(raw_json)
        self.id = self.parsed.id
        self.name = self.parsed.name
        self.objectKey = self.parsed.objectKey
        self.objectSchema = self.parsed.objectSchema
        self.created = self.parsed.created
        self.updated = self.parsed.updated
        self.hasAvatar = self.parsed.hasAvatar
        self.attributes = self.parsed.attributes

    def dump(self):
        """
        Print the raw object to console
        """
        print(self.raw)

    def attribute_value_by_name(self, name, first_found=True):
        """
        Get the value of a specific attribute for the object

        Args:
            name (str): Name of the attribute to get the value
            first_found (bool, optional): Defaults to true, will return onlyt the first attribute found.

        Returns:
            value (str): Value of the given attribute
            values (str[]): All values in an array if first_found is False
        """
        for attr in self.attributes:
            if attr.objectTypeAttribute.name == name:
                if first_found:
                    return attr.objectAttributeValues[0].value
                else:
                    return attr.objectAttributeValues
        raise Exception(f"No attributes with name {name} found.")

    def attribute_id_by_name(self, name, first_found=True):
        """
        Get the id of an attribute by name.

        Args:
            name (str): The attribute to search
            first_found (bool, optional): Defaults to true, will return onlyt the first attribute found.

        Returns:
            value (str): Id of the given attribute
            values (str[]): All values in an array if first_found is False
        """
        for attr in self.attributes:
            if attr.objectTypeAttribute.name == name:
                if first_found:
                    return attr.objectTypeAttribute.id
                else:
                    return attr.objectTypeAttribute
        raise Exception(f"No attributes with name {name} found.")
