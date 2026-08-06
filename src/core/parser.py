class CommandParser:
    """
    Converts a text command into a structured dictionary.
    """

    def parse(self, command: str):
        # Remove leading/ trailing spaces
        command = command.strip()

        # Split the command into words
        parts = command.split()

        #Empty command
        if len(parts) == 0:
            raise ValueError("Command cannot be empty.")

        # First Word = action
        action = parts[0].lower()

        #Second Word = object
        obj = parts[1].lower() if len(parts) > 1 else None

        result = {
            "action": action,
            "object": obj,
        }

        #Parse remaining parameters
        for part in parts[2:]:
            if "=" in part:
                key, value = part.split("=", 1)

                #Try Converting numbers
                try:
                    if "." in value:
                        value = float(value)
                    else:
                        value = int(value)
                except ValueError:
                    pass

                result[key] = value

        return result