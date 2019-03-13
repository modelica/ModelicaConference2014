<h2>List of Tutorials</h2>
<p>
    The tutorials are free and take place on Monday, 14:00 – 17:30.
</p>

<p id="1">
    <b>Tutorial 1:</b> (Room: MA1)<br />
    <b>Simulation and Optimization with JModelica.org and CasADi</b>
</p>
<p>
    by Modelon AB (Johan Åkesson (contact) and the JModelica.org team), Lund Center for Control of Complex Engineering Systems (LCCC) (Fredrik Magnusson) and Joel Andersson, developer of CasADi.
</p>
<p>
    Optimization of non-linear dynamic systems is gaining increased industrial adoption. Key applications include trajectory optimization, Model Predictive Control (MPC), model calibration, state estimation, and design/sizing problems. This tutorial is based on a novel interactive tool-chain which combines the expressiveness and user-friendliness of Modelica and the optimization extension Optimica, with the speed, flexibility and robustness of a modern computational framework dedicated to optimization. Several hands on exercises are offered to demonstrate the capabilities of the new tool-chain, including parameter estimation, trajectory optimization and MPC. Two common methods, collocation and multiple shooting, will be used to solve dynamic optimization problems. In addition, simulation of Modelica models using Python scripting will be demonstrated. Pitfalls and challenges encountered in dynamic optimization of industrial processes are high-lighted. The tutorial is based on the open source software JModelica.org, PyFMI/Assimulo and CasADi.
</p>
<!--<p>
    <a href="pdf/Tutorial1Flyer.pdf">More information on tutorial 1</a>
</p>-->

<p id="2">
    <b>Tutorial 2:</b> (Room: MA2)<br />
    <b>Introduction to Modeling, Simulation, Debugging, and Optimization with Modelica using OpenModelica</b>
</p>
<p>
    by Peter Fritzson, Lena Buffoni, Martin Sjölund, Linköpping University, Sweden and Bernhard Bachmann, Fachhochschule Bielefeld, Germany
</p>
<p>
    Object-Oriented modeling is a fast-growing area of modeling and simulation that provides a structured, computer-supported way of doing mathematical and equation-based modeling. Modelica is today the most promising modeling and simulation language in that it effectively unifies and generalizes previous object-oriented modeling languages and provides a sound basis for the basic concepts. The Modelica modeling language is bringing about a revolution in this area, based on its ease of use, visual design of models with combination of lego-like predefined model building blocks, its ability to define model libraries with reusable components, its support for modeling and simulation of complex applications involving parts from several application domains, and many more useful facilities.<br />
    The tutorial presents an object-oriented component-based approach to computer supported mathematical modeling and simulation through the powerful Modelica language and its associated technology. Modelica can be viewed as an almost universal approach to high level computational modeling and simulation.<br />
    The tutorial gives an introduction to the Modelica language to people who are familiar with basic programming concepts. It gives a basic introduction to the concepts of modeling and simulation, as well as the basics of object-oriented component-based modeling for the novice, and an overview of modeling and simulation in a number of application areas. The OpenModelica environment with its graphical user interface and scripting will be used for hands-on exercises.<br />
    Moreover, in parallel, for those who already know Modelica, a session on debugging of equation-based models will be given, as well as a short introduction to dynamic optimization (collocation/multiple shooting) with OpenModelica.
</p>
<!--<p>
    <a href="pdf/Tutorial1Flyer.pdf">More information on tutorial 1</a>
</p>-->

<p id="3">
    <b>Tutorial 3:</b> (Room: MA3)<br />
    <b>Modeling and Simulation of Electrical Drives</b>
</p>
<p>
    By Anton Haumer, Haumer Technical Consulting, and Christian Kral, TGM, Austria
</p>
<p>
    The tutorial starts with an introduction to electric machines. This includes induction machines and permanent magnet synchronous machines. Simple applications of starting and operating the machines will be presented using the Machines packages of the Modelica Standard Library: Electrical.Machines and Magnetic.FundamentalWave.<br />
    The new developments will be discussed: extension to multiphase machines with phase numbers greater than 3, and the quasi static implementation based on time domain phasors for highest performance of long term simulations.<br />
    For operating electric machines at variable speed usually closed loop drives are used.
    The basic principle of a closed loop drive system will be explained.
    For the examples presented in this tutorial a preview version of the newly developed EDrives library will be utilized.
    An overview of the structure of the basic components (machine, power electronics, sensors, control) will be given.
    An introduction to space phasors used in field oriented control is given, followed by an outline of the basics of controlling permanent magnet synchronous machines.<br />
    The torque controlled drive models of a permanent magnet synchronous machine are presented.
    For these drive types the differences between different combinations of inverter and machine models will be compared:
<ul>
    <li>quasi static inverter + quasi static machine</li>
    <li>averaging inverter + transient machine</li>
    <li>switching inverter + transient machine</li>
</ul>
    After these examples the usage of a speed controller is shown.
    These examples will demonstrate the use of predefined records for convenient parameterization of both the machine and the control, based on machine parameters as used in the Modelica Standard Library.
</p>
<!--<p>
    <a href="pdf/Tutorial1Flyer.pdf">More information on tutorial 1</a>
</p>-->

<p id="4">
    <b>Tutorial 4:</b> (Room: MA4)<br />
    <b>Advanced Analysis of Modelica Models using MapleSim and Maple</b>
</p>
<p>
    by Orang Vahid and Stefan Vorkoetter, Maplesoft, Canada
</p>
<p>
    Since its inception, Modelica has held the promise of letting engineers go further with physical modeling than just running simulations. With the connection between MapleSim and Maple, users can create and document their own symbolic and numeric analyses of Modelica models in a rich problem-solving environment, in addition to performing traditional simulations.<br />
    This tutorial will guide you through the process of extracting equations from a Modelica model into a form amenable to a wide range of analysis. Through hands-on exercises, it will provide you with basic skills to solve, analyse, manipulate, and simulate these equations.<br />
    Examples will include: extracting, interrogating, and solving kinematic and dynamic equations from multibody models; creating, manipulating and discretizing PDEs; creating Modelica components from derived equations; setting-up parameter sweeps and optimizations on Modelica models.
</p>
<!--<p>
    <a href="pdf/Tutorial1Flyer.pdf">More information on tutorial 1</a>
</p>-->

<p id="5">
    <b>Tutorial 5:</b> (Room: MA5)<br />
    <b>Modeling Renewable Energy Systems with "Green Building"</b>
</p>
<p>
    by Dipl.-Ing. Torsten Schwan, EA Systems Dresden GmbH and Dipl.-Ing. Christian Kehrer, ITI GmbH
</p>
<p>
    This tutorial outlines the advantages of a dedicated library for modeling environmentally friendly building systems and energy management concepts. Based on the Modelica language, ITI developed the Green Building library for SimulationX in close collaboration with EA Systems and the Dresden University of Technology. This unique library enables simulations of smart home systems for autonomous buildings that are able to handle their inhabitants’ energy demand and all available resources from conventional supplies to renewables.<br />
    The tutorial explains the underlying concept of the Green Building library. It demonstrates available components and usability to create individual layouts of energy efficient buildings accounting for a variety of input data, e.g. consumer demand, climate, e-Mobility and energy prices. Users learn how to model, analyze and compare different system configurations, e.g. regarding energy and life cycle costs (incl. investment, consumption, subsidies, degradation, maintenance), to find the optimal energy management solution.<br />
    Modeling conventional homes, renewable energy charging stations for electric vehicles and multi-zone buildings illustrate the capabilities of ‘Green Building’ and SimulationX.

</p>
<!--<p>
    <a href="pdf/Tutorial1Flyer.pdf">More information on tutorial 1</a>
</p>-->

<p id="6">
    <b>Tutorial 6:</b> (Room: MA6)<br />
    <b>Functional Mockup Interface 2.0 and HiL Applications</b>
</p>
<p>
    by FMI Modelica Association Project, Dassault Systemés, DLR, ITI and Modelon
</p>
<p>
    FMI 2.0 has many important extensions compared to FMI 1.0. This tutorial will give an overview about these new capabilities and the roadmap for the next year. Automotive OEMs and suppliers present FMI use cases and workflows. Leading HiL providers demonstrate the FMI support of their systems.<br />
    The Modelica FMI test package is introduced which contains test cases for connected FMUs. In practical demonstrations it is shown how FMUs with complex interactions such as coupled mechanical systems can be handled using FMI 2.0. The FMI compliance checker will be utilized for testing the conformity with the specification. It will be shown how FMUs generated by different authoring tools are integrated with a HiL platform.<br />
    This tutorial is useful for end users, decision makers and for tool vendors about to implement support for FMI 2.0.
</p>
<!--<p>
    <a href="pdf/Tutorial1Flyer.pdf">More information on tutorial 1</a>
</p>-->