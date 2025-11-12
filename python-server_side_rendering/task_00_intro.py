#!/usr/bin/python3
import sys
import os.path

"""Generates invitations according to
a template, template.txt and
a list of attendees (list of dictionaries)

Each invite created will be called output_X.txt
where X = # of the current iteration, starting from 1
"""


def generate_invitations(template, attendees):
    # verifies template and attendees are the right type
    try:
        isinstance(template, str)
        isinstance(attendees, list)
        (isinstance(inv, dict) for inv in attendees)
    except Exception as e:
        print(f"Error: {str(e)}")
        return

    # verifies template is not empty
    if len(template) == 0:
        print("Template is empty, no output files generated.")

    # verifies attendees list is not empty
    if len(attendees) == 0:
        print("No data provided, no output files generated.")

    for (index, inv) in enumerate(attendees):
        invite = template
        outputFile = f"output_{index}.txt"

        # verifies output file doesn't exist
        if os.path.exists(outputFile):
            print("This file already exists, no output file generated.")
            return

        # gets values and injects them in invite text
        for placeholder in ['name', 'event_title', 'event_date', 'event_location']:
            value = inv.get(placeholder) or "N/A"
            invite = invite.replace(f"{{{placeholder}}}", str(value))

            # writes invite file
            try:
                with open(outputFile, 'w', encoding='utf-8') as invitation:
                    invitation.write(invite)
            except Exception as e:
                print(f"Couldn't write {outputFile}: {e}")
