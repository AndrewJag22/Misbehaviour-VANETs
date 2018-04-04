# Misbehaviour detection in VANETs
### Installation:
For using SUMO with OmNet++ and others, we generally need to build it from source which can be quite cumbersome. But for only SUMO we can simply install it on Ubuntu as:
```
sudo apt-get install sumo sumo-tools sumo-doc
```

We will use the extra generation scripts in SUMO's tools folder.
First find the path to the folder:
```
whereis sumo
```
in my case it was **/usr/share/sumo/** and some other paths too. Check for the existence of the **tools** folder in one of this location. Note down this path.
Set this path as the $SUMO_PATH variable
```
export SUMO_PATH=/path/to/sumo
```

### Running a Scenario:

1. Load the map 
   Go to Openstreetmap.org. Search for the area wanted and Export the map as a **.osm** file

2. Convert the map into a .net.xml file:
    ```    
    netconvert   --osm-files map.osm -o map.net.xml
    ```

3. Generate random trips of vehicles in the generated map:
    ```
    python $SUMO_PATH/tools/randomTrips.py --net-file=map.net.xml  --route-file=map.rou.xml -e 100 -l
    ```

4. Generate the detectors in the map:
    ```
    python $SUMO_PATH/tools/output/generateTLSE3Detectors.py --net-file=map.net.xml --detector-length=10 frequency=10 -o detector.xml
    ```
    This will auto generate detectors on the map and produce an output file called detector.xml. Go     into the file and make the following changes:
    1. remove the extra elements from the <additional> tag
    2. You will see a bunch of detector tags. You can change the default ids to something simpler like : 0,1,2,3,...so on. Also change the output files of the detectors to reflect the ID on the name
    
    By default the detector.xml writes all the readings to a single file. To make data more accessible, step 2 is important.
    
    NOTE: This step is buggy right now. The script sometimes generate the detectors correctly, some times not. It depends on the map you choose. I have included a very small map- only a single intersection with detectors on two lanes. Use the data from this to build the ML model. To generate large data, we will have to either debug this script, or identify the detectors manually(just have to specify the roads we want them in and their pos)


5. Run the scenario as:
    ```
    sumo-gui map.sumocfg
    ```
    This will generate the data in the output files of the detectors. Note that all detectors are producing correct results right now.


6. The xml output files can be easily converted into csv file:
    ```
    python $SUMO_PATH/tools/xml/xml2csv.py --separator=, --output=test.csv <xml-file-name>
    ```


Now select a bunch of random detectors, randomly generate output CSV files with wrong outputs. This way the training data can be generated.


### Additional Notes:
1. In the gui you can see a variety of info. View the dynamic changing values of entities by rightclicking the entity and press show parameters.
2. You can even affect the simulation in real-time. Like closing a lane, or toggling the traffic light.
3. There were a bunch of detectors available. The entry-exit detector is the best bet to gauge the amount of traffic in a particular road segment. You can check-out the other detectors [here](http://sumo.dlr.de/wiki/Simulation/Output#simulated_detectors).
4. The documentation of SUMO can be confusing but it is robust, and covers most of the problems. So if you do not understand anything, just look it up in the docs.