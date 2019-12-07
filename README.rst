2018 Central Park Squirrel Tracker Project
==========================================

By: Project Group29 | Members: Yuanjun Ling, Zhiyuan Chen | UNIs: yl4273, zc2481 | From: Tools for Analytics sec001

.. contents::

Project description
-------------------

The project takes the 2018 central park squirrel data and track of all the known squirrels in the central park.

The project provides several features based on Django and gcloud deployment.

Features included:

- Located at: / 
A view that gives the guide of the whole project
- Located at: /map
A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map.
- Located at: /sightings    A view that lists all squirrel sightings with links to edit each
- Located at: /sightings/<unique_squirrel_id>   A view to update a particular squirrel sighting
- Located at: /sightings/add    A view to create a new squirrel sighting
- Located at: /sightings/stas   A view with general stats about the sightings

It is allowed to import new up-to-date squirrel csv data and export the current data into a csv format through management commands::

    $ python manage.py import_squirrel_data /path/to/file.csv
    $ python manage.py export_squirrel_data /path/to/file.csv

Group Information
-----------------

Project Group 29, Tools for Analytics Section 1

Members: Yuanjun Ling, Zhiyuan Chen

UNIs: [yl4273, zc2481]

Links to the project
--------------------

- Link to the repository for the project source code: https://github.com/ZhiyuanChen1017/project29
- Public git clone URL: https://github.com/ZhiyuanChen1017/project29.git
- Link to the server running the application: https://virtual-machine-255421.appspot.com/
