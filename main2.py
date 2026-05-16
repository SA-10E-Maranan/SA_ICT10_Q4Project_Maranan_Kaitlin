from pyscript import document, display
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

days = []
absences = []

def displaying(e):
    day = document.getElementById('dayOfTheWeek').value
    absence = int(document.getElementById('absences').value)

    days.append(day)
    absences.append(absence)

    converted_absences = np.array(absences)

    # Clear previous graph
    plt.clf()

    # Create graph
    fig, ax = plt.subplots(figsize=(5.5, 3.5))

    ax.plot(days, converted_absences, marker='o')
    ax.set_title("Weekly Attendance (Absences)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Number of Absences")
    ax.grid(True)

    fig.tight_layout()

    # Clear old graph
    document.getElementById("output").innerHTML = ""

    # Display inside output div
    display(fig, target="output")
