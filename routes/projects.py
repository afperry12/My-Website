# routes/projects.py
from flask import Blueprint, render_template

bp = Blueprint('projects', __name__)

@bp.route('/projects')
def projects():
    projects = [
        {
            "name": "Neuroscience Project",
            "description": "A 3D interactive brain map built with Unity and WebGL, featuring labeled parts of the brain including the Corpus Callosum, Left Ventricle, Right Ventricle, Thalamus, Hypothalamus, Midbrain, Pons, Central Sulcus, Precentral Gyrus, Primary Motor Cortex, Premotor Cortex, Postcentral Gyrus, and Primary Somatosensory Cortex. The map also includes summaries of three scientific papers on the effects of ethanol on the cerebellum, the impact of sleep deprivation on ability to function, and predicting motor intentions based on neuronal signal patterns. Users can fly around the brain and access definitions and abstracts by clicking on various parts of the map.",
            "link": "/brainmap",
            "date": "October 2021"
        },
        {
            "name": "Space Agents Video Game",
            "description": "In this project, I built my own custom network solution to creating a 3D video game. I wanted to be in control of every part of the process. So, I modeled my own humanoid game character and even did the bone rigging for it myself in Blender. I learned about creating, sending, and receiving packets. I learned about different methods of handling client-server architectures. I also learned how to build my own game launcher and inject authentication into the game on start",
            "link": "/spaceagents",
            "date": "July 2021"
        },
        {
            "name": "Project C",
            "description": "A description of Project C",
            "link": "https://www.example.com/project-c"
        }
    ]
    return render_template('projects.html', projects=projects)
