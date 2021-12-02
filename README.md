# Capstone-Generator

## Table of Contents

- [Generator Design](https://github.com/lhange42/Capstone-Generator/blob/main/README.md#generator-design)
  * [Assembly](https://github.com/lhange42/Capstone-Generator/blob/main/README.md#description-of-assembly)
  * [Research](https://github.com/lhange42/Capstone-Generator/blob/main/README.md#research)
- [CAD](https://github.com/lhange42/Capstone-Generator/blob/main/README.md#cad)
  * [Box](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#capsule)
    + [Part not made](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#top-sphere)
    + [Part not made](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#bottom-sphere)
    + [Part not made](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#components)
    + [Assembly](https://github.com/lhange42/Capstone-Generator/blob/main/README.md#assembly)
    + [Reflections](https://github.com/lhange42/Capstone-Generator/blob/main/README.md#reflections)
  * [Generator](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#trebuchet)
    + [Part not made](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#basic-joints-and-connection-pieces)
    + [Part not made](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#3d-printed-joints)
    + [Part not made](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#finger-piece)
    + [Part not made](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#release-mechanism)
    + [Part not made](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#axle-cap)
    + [Part not made](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#other-components)
    + [Part not made](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#full-trebuchet-assembly)
- [Code](https://github.com/lhange42/Capstone-Generator/blob/main/README.md#code)
  * [FuncAngleOMeter](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#funcangleometer)
  * [Index](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#index)
  * [Get Angle Test](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#get-angle-test)
- [Physical Assembly](https://github.com/lhange42/Capstone-Generator/blob/main/README.md#physical-assembly)
  * [Capsule](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#capsule)
  * [Trebuchet](https://github.com/omckenn37/EG4_Trebuchet/blob/main/README.md#trebuchet)
- [Results and Overall Reflections](https://github.com/lhange42/Capstone-Generator/blob/main/README.md#results-and-overall-reflections)

## Generator Design
<p float="left">
	<img src="Media/Planning/Center_Ring_of_Solenoids.png" Height="200">
	<img src="Media/Planning/Magnet_Plate.PNG" Height="200">
	<img src="Media/Planning/bearing_face_diagram.PNG" Height="200">
	<img src="Media/Planning/Coil_Ring.PNG" Height="200">
</p>

### Description of Assembly

The first picture on the left is showing the center of the generator which will be composed of two laser cut plates and 8 solenoids. These solenoids will be held in place by the circular slots in the laser cut piece that will equal the radius of the smaller section of the solenoid. However, this plan is one of the first ideas and our new idea is to make a friction fit layer of three plates that will hold 8 coils; we are doing this to create less separation between the magnets and the coils. The two laser-cut plates will be screwed together so the solenoids are tightly held in between them. The second picture is a sheet of laser cut material and the thickness of the laser cut material is the exact same as the magnets so this will make it easy to stack plates to make our magnets securely harnessed. In terms of generator diction, our center ring of coils will bet the stator of the generator since it’s stationary and just harnessing power while the ring of magnets is going to be the rotor since it will be attached to the rotating axis and spinning with it.

### Research
#### Magnetic Induction
Magnetic induction is how we are going to produce voltage with our generator. Magnetic Induction is when alternating magnetic poles induce an electrical current. So as our generator harnesses rotational motion and spins the plates that contain the magnets around the coils it will induce a current in the coils. This voltage is formed through the magnetic fields going through the magnetic flux of the coil which produces energy because flux creates energy from anything passing through its field. This is why our generator will originally produce an alternating current because as the magnets rotate and the polls flip the direction of the voltage will also flip. This is all found by Micahel Faraday who created a formula to calculate an emf or electromotive force; specifcally used to calculate the instantaneous voltage because it can be different depending on the point you read it at. 
#### Circuit Divider
A circuit divider basically is a system of two resistors in which if you position the wires correctly,  one between the resistors and one after the second one,  that the voltage going through those wires will be less than the voltage in the whole circuit, and as you change the ratio of the resistors the amount that the voltage is divided by is increased. To divide your voltage by the greatest amount you want to make the first resistor a lot larger than the second resistor. We are planning on testing our generator and finding out the maximum voltage then setting up a circuit divider that will guarantee a voltage under 5V so the pi can read it, since the pi only reads 0V to 5V, and to compensate the voltage divider we will just multiply the value read by the value that voltage divider divides it by to return it to its true voltage. A circuit divider is going to be mandatory for the methodology of our project we are going to need to be able to read the voltage of the generator in some form that will communicate with the pi because it’s the focus of the coding part of our project. 




## CAD



##### Coil Mold
<p float="left">
	<img src="Media/CAD/Coil_Assembly.PNG" Height="200">
	<img src="Media/CAD/Coil_Caps.PNG" Height="200">
	<img src="Media/CAD/Coil_Center.PNG" Height="200">
</p>
###### Description
This is going to be used to form our coils. They are constructible solenoids with detachable ends. We plan on them being attachable to drills so we can spin and coil the solenoid. Then once the coil is made and fastened together so it doesn’t become uncoiled we can detach the ends by rotating them until the slot lines up and then its just constructed around the center that we can detach.

#### Assembly
<p float="left">
  <img src="media/AssemblyWithoutTopCircle.png" Height="200">
  <img src="media/AssemblyWithoutBottomCircle.png" Height="225">
  <img src="media/FullAssembly.png" Height="225">
  <img src="media/Assembly_Labeled_picture.png" Height="225">
</p>


<br>

#### Reflections 


---

### Generator

#### Basic Joints and Connection Pieces

<p float="left">
  <img src="media/oldjointpic.png" height="200">
  <img src="media/bracket68pic.png" height="200">
  <img src="media/twowaybracketpic.png" height="200">
  <img src="media/middlebracketpic.png" height="200">
</p>



#### 3D Printed Joints

<p float="left">
  <img src="media/bearingjointpic.png" height="300">
  <img src="media/bearingjointpic2.png" height="300">
  <img src="media/counterweightjointpic.png" height="300">
</p>

#### part

<p float="left">
  <img src="media/fingerpiecepic.png" height="340">
  <img src="media/fingerswivelpic.png" height="340">
  <img src="media/fingerassemblypic1.png" height="340">
  <img src="media/fingerassemblypic2.png" height="340">
</p>



#### part

<p float="left">
  <img src="media/releasemechpic1.png" height="300">
  <img src="media/releasemechpic2.png" height="300">
</p>


#### part

<img src="media/axlecappic.png" height="200">


#### Other Components

##### Coil


##### Nuts & Bolts


##### Bearings


##### Steel Rod


#### Full Generator Assembly

<img align="right" src="media/trebuchetannotatedpic.png" width="600">



<p float="left">
  <img src="media/fulltrebuchetpic1.png" height="260">
  <img src="media/fulltrebuchetpic2.png" height="260">
  <img src="media/fulltrebuchetpic3.png" height="260">
  <img src="media/fulltrebuchetpic4.png" height="260">
  <img src="media/fulltrebuchetpic5.png" height="260">
</p>

---


## Code









### program

T

<details>
<summary>Code</summary>
<!--All you need is a blank line-->

**Python** *Code*
```python
#code goes here

```
</details>

### Index


	
<details>
<summary>Code</summary>
<!--All you need is a blank line-->

**Python** *Code*
```python
#code goes here

```
</details>

	
## Physical Assembly
### Capsule
	
#### Inner Generator
<p float="left">
  <img src="media/CapsulePhysicalAssembly1.png" height="250">
  <img src="media/CapsulePhysicalAssembly2.png" height="250">
  <img src="media/CapsulePhysicalAssembly3.png" height="250">
</p>

	
#### part 1
<img src="media/Top_Circle_Printed.png" height="300">
	
#### Components of the generator
<img src="media/PiCapsule.png" Height="300">	

### box


<p float="left">
<img src="media/tr1.JPG" height="250">
<img src="media/tr2.JPG" height="250">
<img src="media/tr3.JPG" height="250">
<img src="media/tr4.JPG" height="250">
<img src="media/tr5.JPG" height="250">
<img src="media/tr6.JPG" height="250">
<img src="media/tr7.JPG" height="250">

</p>
	
## Results and Overall Reflections
	

