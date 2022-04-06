## Project Plan

For more info check .pdf file in the repository root.


1. Team name and team members (up to 4 persons/team)

    DancingQueens -
    Jesse Järvi, Roope Pouta, Eetu Rantala, Antti Auranen

2. Application / Use-case
    
    We will be doing synchronized choreography with a Tello drone and a Jetbot. We will
    set it up in a way that the Tello drone identifies objects or colors, and then passes the
    data to the Jetbot, which then uses a set of dance moves matching the given
    parameters.

3. The system
    
    Tello, Jetbot, ros2, open cv, jetson, visual studio code, github...
    We will be using Tello drone and Jetbot as our devices. I don’t think that we need
    any additional sensor, only the camera that is included in the tello drone.
    As for algorithms I think we will use basic object detection or color detection
    softwares in the Tello drone. For Jetbot we will be using basic movement commands.

    IMG

4. GitHub repo link

    https://github.com/ranzuh/ras_project

5. Background
    
    We all are rather familiar with jetbots from previous courses, and doing some kind of
    detection with the tello drone as we did in the previous course where we had to
    implement face detection to the tello drone and make it follow your face in a certain
    distance. After the first assignment in this course we then have experience with
    detecting shapes and also faces with the drone, so that comes in handy when trying
    to detect the certain signals for our jetbot. Also moving the jetbot and giving it simple
    moving commands we have covered quite many times now.
    Probably the riskiest or at least the part that we have least amount of experience is
    the communication between these two devices. But as we are sending just simple
    messages I think we can handle that.

6. Expected challenges and wishes to learn
    
    We expect the main challenges to be in the Tello drone phase. Image recognition is
    something that we’ve practiced, but it can be a bit tricky sometimes. Also, making the
    bot work together in the network could prove to be difficult, as it is something we’ve
    never done before this project. I think that at least making the Tello pass through
    some of the tracks is useful in completing the project, and libraries that we will use
    are probably at least somewhat familiar to everyone. Our project as is will probably
    not require additional sensors.

7. Team roles
    
    Eetu is our main developer.
    Roope & Jesse will be all around guys, helping with coding, testing and writing
    documents.
    Antti will be our main document guy and focusing mainly on the report.

8. Work packages (how is the work going to be divided among team members and in time), with tentative project schedule.
    
    We cannot say how we will be dividing our actual efforts, it will be more clearer later
    and we can then update this document based on how things pan out.

9. Description of final experiment or demonstration.
    
    I think the plan is to set some objects or colors, for example an top of bookshelf,
    drone is then supposed to fly up there and recognize these colors and send certain
    commands to the jetbot according to what the image or color was (as in example red
    ball could be “spin 360”).