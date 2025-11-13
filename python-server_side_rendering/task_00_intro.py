import os

def generate_invitations(template, attendees):
    # check input types
    if not isinstance(template, str):
        raise TypeError("Template must be a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        raise TypeError("Attendees must be a list of dictionaries")
        return
   
    # handle empty inputs
    if not template:
        raise ValueError("Template is empty, no output files generated.")
        return
    if not attendees:
        raise ValueError("No data provided, no output files generated.")
        return
    
    index = 0
    template_copy = template
    # create a new dict with "N/A" for missing or None values
    for attendee in attendees:
        template = template_copy
        for key, value in attendee.items():
            if value == None:
                template = template.replace('{' + key + '}', "N/A")
            else:
                template= template.replace('{' + key + '}', value)

        # write to file
        index = index + 1
        path = "output_" + str(index) + ".txt"
        if os.path.exists(path):
            print(f"File {path} already exists")
        else:
            with open(path, "w") as file:
                file.write(template)
