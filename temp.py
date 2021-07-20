import numpy as np


paper = ['S.-K. Lee and J.-H. Kim, “Air-Text: Air-Writing and Recognition System,” Proc. 2021  Association for Computing Machinery Multimedia (ACM-MM), Oct. 2021.',

'S.-M. Yoo, U.-H. Kim and Y. Hwang and J.-H. Kim, “Type Anywhere You Want: An Introduction to Invisible Mobile Keyboard,” Proc. 2021 International Joint Conference on Artificial Intelligence (IJCAI), Aug. 2021.',

'J. Kim, I. Yoon, G.-M. Park, and J.-H. Kim. “Non-probabilistic cosine similarity loss for few-shot image classification,” in The 31st British Machine Vision Conference (BMVC), Virtual, Sep. 2020.',

'S.-J. Lee, J.-M. Park and D.-H. Kim and J.-H. Kim, “Adaptive Task Planner for Performing Home Service Tasks in Cooperation with a Human,” Proc. 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2018.',

'W.-H. Lee and J.-H. Kim, “Social Relationship Development between Human and Robot through Real-time Face Identification and Emotional Interaction,” in Proc. ACM/IEEE International Conference on Human Robot Interaction, Video Abstract, (Best Video Award), Mar. 2018.',

'S.-H. Cho, W.-H. Lee and J.-H. Kim, “Implementation of Human-Robot VQA Interaction System with Dynamic Memory Networks,” in Proc. 2017 IEEE International Conference on Systems, Man, and Cybernetics, (Best Student Paper Award), Banff Center, Banff, Canada, Oct. 2017.',

'D. Sigmund, G.-M. Park and J.-H. Kim, “Context Preference-based Deep Adaptive Resonance Theory: Integrating User Preferences into Episodic Memory Encoding and Retrieval,” IEEE International Joint Conference on Neural Networks, May. 2017.',

 
'S. Gulshad, D. Sigmund and J.-H. Kim, “Learning to Reproduce Stochastic Time Series Using Stochastic LSTM,” IEEE International Joint Conference on Neural Networks, May. 2017.',

 
'S. Gulshad and J.-H. Kim, “Deep Convolutional and Recurrent Writer,” IEEE International Joint Conference on Neural Networks, May. 2017.',

 
'J.-M. Park J.-H. Kim, “Online recurrent extreme learning machine and its application to time-series prediction,” IEEE International Joint Conference on Neural Networks, May. 2017.',

 
'B.-S. Ko, H.-J. Choi, C.-S. Hong, J.-H. Kim, O.-C. Kwon and C.-D. Yoo, “Neural network-based autonomous navigation for a homecare mobile robot,” IEEE International Conference on Big Data and Smart Computing (BigComp), pp. 403-406, Feb. 2017.',

 
'M.-J. Kim, S.-H. Baek, S.-H. Cho and J.-H. Kim, “Approach to Integrate Episodic Memory into Cogency-based Behavior Planner for Robots,” in Proc. 2016 IEEE International Conference on Systems, Man, and Cybernetics, Oct. 2016.',

 
'G.-M. Park, S.-H. Cho and J.-H. Kim, “Biologically-Inspired Episodic Memory Model Considering the Context Information,” in Proc. 2016 IEEE International Conference on Systems, Man, and Cybernetics, Oct. 2016.',

 
'Y.-H. Yoo, D.-H. Kim, G.-M. Park, I.-B. Jeong, S.-H. Baek, S.-J. Ryu and and J.-H. Kim, “Memory-based Realization of Task Intelligence for Robots in Human Environment,” Assistance and Service Robotics in a Human Environment Workshop in conjunction with IEEE/RSJ International Conference on Intelligent Robots and Systems, Daejeon, Korea, Oct. 2016.',

 
'S.-H. Cho, S.-H. Baek, D.-H. Kim, Y.-H. Yoo and J.-H. Kim, “Cogent Confabulation-based Hierarchical Behavior Planner for Task Performance,” in Proc. 2016 IEEE International Conference on Systems, Man, and Cybernetics, Oct. 2016.',

 
'S.-H. Baek, S.-J. Ryu and J.-H. Kim, “DMQEA-FCM: an Approach for Preference-based Decision Support,” in Proc. 2016 IEEE World Congress on Computational Intelligence, Vancouver, Canada, Jul. 2016.',

 
'U.-H. Kim and J.-H. Kim, “A Fuzzy Expert System for Designing Customized Workout Programs,” in Proc. 2016 IEEE World Congress on Computational Intelligence, Vancouver, Canada, Jul. 2016.',

 
'G.-M. Park and J.-H. Kim, “Deep Adaptive Resonance Theory for Learning Biologically Inspired Episodic Memory,” in Proc. 2016 IEEE World Congress on Computational Intelligence, Vancouver, Canada, Jul. 2016.',

 
'J.-Y. Park, Y.-H. Yoo, D.-H. Kim and J.-H. Kim, “Integrated Adaptive Resonance Theory Neural Model for Episodic Memory with Task Memory for Task Performance of Robots,” in Proc. 2016 IEEE World Congress on Computational Intelligence, Vancouver, Canada, Jul. 2016.',

 
'J.-Y. Park, W.-R. Ko and J.-H. Kim, “Multimedia Recommendation System Using Adaptive Resonance Theory Neural Model for Digital Storytelling,” in Proc. 2016 IEEE World Congress on Computational Intelligence, Vancouver, Canada, Jul. 2016.',

 
'C.-S. Hong, C.-W. Park and J.-H. Kim, “Evolutionary Dual Rule-based Fuzzy Path Planner for Omnidirectional Mobile Robot,” in Proc. 2016 IEEE World Congress on Computational Intelligence, Vancouver, Canada, Jul. 2016.',

 
'D. Sigmund and J.-H. Kim, “Reference Point-based Nondominated Sorting Multi-objective Quantum-inspired Evolutionary Algorithm,” in Proc. 2016 IEEE World Congress on Computational Intelligence, Vancouver, Canada, Jul. 2016.',

 
'Y.-H. Yoo and J.-H. Kim, “Procedural Memory Learning from Demonstration for Task Performance,” in Proc. IEEE International Conference on Systems, Man and Cybernetics, Oct. 2015.',

 
'S.-B. Han, D.-H. Kim and J.-H. Kim, “Fuzzy Gaze Control-based Navigation Assistance System for Visually Impaired People in a Dynamic Indoor Environment,” in Proc. 2015 IEEE International Conference on Fuzzy Systems, Istanbul, Turkey, Aug. 2015.',

 
'K.-B. Lee and J.-H. Kim, “DMOPSO: Dual Multi-Objective Particle Swarm Optimization,” in Proc. 2014 IEEE World Congress on Computational Intelligence, Beijing, China, Jun. 2014.',

 
'S.-J. Ryu and K.-B. Lee and J.-H. Kim, “Improved Version of a Multiobjective Quantum-inspired Evolutionary Algorithm with Preference-based Selection,” in Proc. 2012 IEEE World Congress on Computational Intelligence, Brisbane, Australia, Jun. 2012.',

 
'I.-W. Park and K.-B. Lee and J.-H. Kim, “Multi-objective Evolutionary Algorithm-based Optimal Posture Control of Humanoid Robots,” in Proc. 2012 IEEE World Congress on Computational Intelligence, Brisbane, Australia, Jun. 2012.',

 
'I.-W. Park, Y.-D. Hong and B.-J. Lee and J.-H. Kim, “Generating Optimal Trajectory of Humanoid Arm that Minimizes Torque Variation using Differential Dynamic Programming,” in Proc. IEEE International Conference on Robotics and Automation, Saint Paul, USA, May. 2012.',

 
'S.-J. Ryu and J.-H. Kim, “Classification of Long-term Motions Using a Two-layered Hidden Markov Model in a Wearable Sensor System,” in Proc. IEEE International Conference on Robotics and Biomimetics (ROBIO), Thailand, Dec. 2011.',
 
'C.-S. Park, Y.-D. Hong and J.-H. Kim, “An Evolutionary Central Pattern Generator for Stable Bipedal Walking by the Increased Double Support Time,” in Proc. IEEE International Conference on Robotics and Biomimetics (ROBIO), Thailand, Dec. 2011.',

 
'D.-H. Lee, J.-H. Han and J.-H. Kim, “A Preference-based Task Allocation Framework for Multi-Robot Coordination,” in Proc. IEEE International Conference on Robotics and Biomimetics (ROBIO), Tailand, Dec. 2011.',

 
'Y.-D. Hong and J.-H. Kim, “3-D Command State-Based Modifiable Walking of a Humanoid Robot on Uneven Terrain with Different Inclinations and Heights,” in Proc. IEEE International Conference on Robotics and Biomimetics (ROBIO), Phuket, Thailand, Dec. 2011.',

 
'Y.-D. Hong, C.-S. Park and J.-H. Kim, “Human-Like Stable Bipedal Walking with a Large Stride by the Height Variation of the Center of Mass using an Evolutionary Optimized Central Pattern Generator,” in Proc. Annual Conference on IEEE Industrial Electronics Society (IECON), Melbourne, Australia, Nov. 2011.',

 
'I.-W. Park and J.-H. Kim, “Estimating Entire Geometric Parameter Errors of Manipulator Arm Using Laser Module and Stationary Camera,” in Proc. Annual Conference on IEEE Industrial Electronics Society (IECON), Melbourne, Australia, Nov. 2011.',

 
'W.-R. Ko, H.-S. Hyun, H.-J. Kim, S.-H. Choi and and J.-H. Kim, “Behavior Selection Method for Intelligent Artificial Creatures Using Degree of Consideration-based Mechanism of Thought,” in Proc. IEEE International Conference on Systems, Man and Cybernetics, Oct. 2011.',

 
'Sheir Afgen Zaheer and Jong-Hwan Kim, “Type-2 Fuzzy Airplane Altitude Control: a Comparative Study,” in Proc. IEEE International Conference on Fuzzy Systems, Jun. 2011.',

 
'Bum-Soo Yoo and Se-Hyoung Cho and Jong-Hwan Kim, “Fuzzy Integral-based Composite Facial Expression Generation for a Robotic Head,” in Proc. IEEE International Conference on Fuzzy Systems, Jun. 2011.',

 
'In-Bae Jeong, Chang-Soo Park, Ki-In Na, Seungbeom Han and Jong-Hwan Kim, “Particle Swarm Optimization-based Central Patter Generator for Robotic Fish Locomotion,” in Proc. IEEE Congress on Evolutionary Computation, Jun. 2011.',

 
'Lee Ki-Baek and Kim Jong-Hwan, “Multi-Objective Particle Swarm Optimization with Preference-based Sorting,” in Proc. IEEE Congress on Evolutionary Computation, Jun. 2011.',

 
'Dong-Hyun Lee and Jong-Hwan Kim, “A Framework for an Interactive Robot-based Tutoring System and Its Application to Ball-passing Training,” in Proc. IEEE International Conference on Robotics and Biomimetics, Dec. 2010.',

 
'Y.-D. Hong and J.-H. Kim, “A Novel Modifiable Walking Pattern Generator on an Inclined Plane in Pitch and Roll Directions for Humanoid Robots,” in Proc. IEEE International Conference on Robotics and Biomimetics (ROBIO), Tianjin, China, Dec. 2010.',

 
'Ki-In Na, Chang-Soo Park, In-Bae Jeong, Seungbeom Han and Jong-Hwan Kim, “Locomotion Generator for Robotic Fish Using an Evolutionary Optimized Central Pattern Generator,” in Proc. IEEE International Conference on Robotics and Biomimetics, Dec. 2010.',

 
'Ji-Hyeong Han and Jong-Hwan Kim, “Human-Robot Interaction by Reading Human Intention based on Mirror-Neuron System,” in Proc. IEEE International Conference on Robotics and Biomimetics, Tianjin, China, pp. 561-566, Dec. 2010.',

 
'Jeong-Ki Yoo and Jong-Hwan Kim, “Navigation Framework for Humanoid Robots Integrating Gaze Control and Modified-univector Field Method to Avoid Dynamic Obstacles,” in Proc. IEEE International Conference on Intelligent Robots and Systems, Taipei, Taiwan, pp.1683-1689, Oct. 2010.',

 
'C.-S. Park, Y.-D. Hong and and J.-H. Kim, “Full-body Joint Trajectory Generation Using an Evolutionary Central Pattern Generator for Stable Bipedal Walking,” in Proc. IEEE International Conference on Intelligent Robots and Systems (IROS), Taipei, Taiwan, Oct. 2010.',

 
'In-Won Park, Bum-Joo lee, Ye-Hoon Kim, Ji-Hyeong Han and Jong-Hwan Kim, “Multi-objective Quantum-inspired Evolutionary Algorithm-based Optimal Control of Two-link Inverted Pendulum,” in Proc. 2010 IEEE World Congress on Computational Intelligence, Barcelona, Spain, pp. 3382-3388, Jul. 2010.',

 
'Hyungmin Park, Ji-Hyeong Han and Jong-Hwan Kim, “Swarm Intelligence-based Sensor Network Deployment Strategy,” in Proc. 2010 IEEE World Congress on Computational Intelligence, Barcelona, Spain, pp. 4210-4215, Jul. 2010.',

 
'Y.-D. Hong, Y.-H. Kim and J.-H. Kim, “Evolutionary Optimized Footstep Planning for Humanoid Robot,” in Proc. IEEE International Symposium on Computational Intelligence in Robotics and Automation (CIRA), Daejeon, Korea, Dec. 2009.',

 
'Dong-Hyun Lee, In-Won Park and Jong-Hwan Kim, “Q-learning using Fuzzified States and Weighted Actions and Its Application to Omni-directional Mobile Robot Control,” in Proc. 2009 IEEE International Symposium on Computational Intelligence in Robotics and Automation, Daejeon, Korea, pp. 102-107, Dec. 2009.',

 
'J.-H. Kim, S.-H. Choi, Duckhwan Kim, Joonwoo Kim and Minjoo Cho, “Animal-Robot Interaction for Pet Caring,” in Proc. 2009 IEEE International Symposium on Computational Intelligence in Robotics and Automation, Daejeon, Korea, pp. 598-603, Dec. 2009.',

 
'Feng Xiao, Ming Yuchi, Ming-yue Ding, Jun Jo and Jong-Hwan Kim, “A Multi-step Heart Rate Prediction Method Based on Physical Activity Using Adams-Bashforth Technique,” in Proc. 2009 IEEE International Symposium on Computational Intelligence in Robotics and Automation, Daejeon, Korea, pp. 355-359, Dec. 2009.',

 
'Y.-H. Kim and and J.-H. Kim, “Multiobjective Quantum-inspired Evolutionary Algorithm for Fuzzy Path Planning of Mobile Robot,” in Proc. IEEE Congress on Evolutionary Computation, Norway, Trondheim, pp. 1185-1192, May. 2009.',

 
'K.-B. Lee and and J.-H. Kim, “Particle Swarm Optimization Driven by Evolving Elite Group,” in Proc. IEEE Congress on Evolutionary Computation, Norway, Trondheim, pp. 2114-2119, May. 2009.',

 
'Yong-Duk Kim, In-Won Park, Jeong-Ki Yoo and Jong-Hwan Kim, “Stabilization Control for Humanoid Robot to Walk on Inclined Plane,” 2008 8th IEEE-RAS International Conference on Humanoid Robots, pp. 28-33, Dec. 2008.',

 
'In-Bae Jeong and Jong-Hwan Kim, “Multi-Layered Architecture of Middleware for Ubiquitous Robot,” in Proc. 2008 IEEE International Conference on Systems, Man and Cybernetics (SMC 2008), pp. 3479-3484, Oct. 2008.',

 
'In-Won Park, Jong-Hwan Kim and Kui-Hong Park, “Accelerated Q-Learing for Fail State and Action State,” in Proc. 2008 IEEE International Conference on Systems, Man and Cybernetics (SMC 2008), pp. 764-767, Oct. 2008.',

 
'Sunglok Choi and Jong-Hwan Kim, “Robust Regression to Varying Data Distribution and Its Application to Landmark-based Localization,” in Proc. 2008 IEEE International Conference on Systems, Man and Cybernetics (SMC 2008), pp. 3465-3470, Oct. 2008.',

 
'Hyungmin Park and Jong-Hwan Kim, “Potential and Dynamics based Particle Swarm Algorithm,” in Proc. IEEE Congress on Evolutionary Computation, Hong Kong, Jun. 2008.',

 
'Dong-Hyun Lee and Jong-Hwan Kim, “Evolutionary Personalized Robotic Doll: GomDoll,” in Proc. IEEE Congress on Evolutionary Computation, Hong Kong, Jun. 2008.',

 
'Ki-Baek Lee and Jong-Hwan Kim, “Mass-spring-damper Motion Dynamics-based Particle Swarm Optimization,” in Proc. IEEE Congress on Evolutionary Computation, Hong Kong, Jun. 2008.',

 
'Chi-Ho Lee, Ye-Hoon Kim and Jong-Hwan Kim, “Multiobjective Evolutionary Algorithm Reinforcing Specific Objective,” in Proc. IEEE Congress on Evolutionary Computation, Hong Kong, Jun. 2008.',

 
'B.-J. Lee, D. Stonier, Y.-D. Kim, J.-K. Yoo and J.-H. Kim, “Modifiable Walking Pattern Generation using Real-Time ZMP Manipulation for Humanoid Robots,” in Proc. IEEE International Conference on Intelligent Robots and Systems, San Diego, USA, Nov. 2007.',

 
'Chi-Ho Lee, Kang-Hee Lee and Jong-Hwan Kim, “Evolutionary Multi-Objective Optimization for Generating Artificial Creature’s Personality,” in Proc. IEEE Congress on Evolutionary Computation, Singapore, pp. 2450-2455, Sep. 2007.',

 
'Y.-H. Kim, S.-H. Cho, S.-H. Choi and J.-H. Kim, “Software Robot in a PDA for Human Interaction and Seamless Service,” in Proc. IEEE International Symposium on Robot & Human Interactive Communication, Jeju, Korea, pp. 969-973, Aug. 2007.',

'I.-W. Park, Y.-D. Kim, B.-J. Lee, J.-K. Yoo and J.-H. Kim, “Generating Performance Motions of Humanoid Robot for Entertainment,” in Proc. IEEE International Symposium on Robot & Human Interactive Communication, Jeju, Korea, Aug. 2007.',

 
'Dong-Hyun Lee, Ki-Baek Lee and Jong-Hwan Kim, “Reflex and Emotion-based Behavior Selection for Toy Robot,” in Proc. IEEE International Symposium on Robot & Human Interactive Communication, Jeju, Korea, Aug. 2007.',

 
'S.-H. Cho, Y.-H. Kim, I.-W. Park and J.-H. Kim, “Behavior Selection and Memory-based Learning for Artificial Creature Using Two-layered Confabulation,” in Proc. IEEE International Symposium on Robot & Human Interactive Communication, Jeju, Korea, pp 992-997, Aug. 2007.',

'J.-H. Kim, C.-H. Lee, K.-H. Lee and N. S. Kuppuswamy, “Evolving Personality of a Genetic Robot in Ubiquitous Environment,” in Proc. IEEE International Symposium on Robot & Human Interactive Communication, Jeju, Korea, pp. 848-853, Aug. 2007.',

 
'J.-H. Kim, K.-H. Lee, Y.-D. Kim, N. S. Kuppuswamy and J. Jo, “Ubiquitous Robot: A New Paradigm for Integrated Services,” in Proc. IEEE International Conference on Robotics and Automation, Roma, Italy, pp. 2853-2858,, Apr. 2007.',

 
'D. Stonier, S.-H. Cho, S.-L. Choi, N. S. Kuppuswamy and J.-H. Kim, “Nonlinear Slip Dynamics for an Omniwheel Mobile Robot Platform,” in Proc. IEEE International Conference on Robotics and Automation, Roma, Italy, pp. 2367-2372, Apr. 2007.',

 
'Y.-D. Kim, B.-J. Lee, J.-K. Yoo, J.-H. Kim and J.-H. Ryu, “Landing Force Controller for a Humanoid Robot: Time-Domain Passivity Approach,” in Proc. IEEE International Conference on Systems, Man and Cybernetics, Taiwan, pp. 4237-4242, Oct. 2006.',

 
'T.-H. Kim, S.-H. Choi and J.-H. Kim, “Middle Layer Incorporating Software Robot and Mobile Robot,” in Proc. IEEE International Conference on Systems, Man and Cybernetics, Taiwan, pp. 253-259, Oct. 2006.',

 
'D. Stonier and J.-H. Kim, “ZMP Analysis for Realisation of Humanoid Motion on Complex Topologies,” in Proc. IEEE International Conference on Systems, Man and Cybernetics, Taiwan, pp. 247-252, Oct. 2006.',

 
'J.-S. Jang and J.-H. Kim, “Evolutionary Pruning for Fast and Robust Face Detection,” in Proc. IEEE Congress on Evolutionary Computation, Vancouver, Canada, pp. 4436-4442, Jul. 2006.',

 
'K.-H. Han and J.-H. Kim, “On the Analysis of the Quantum-inspired Evolutionary Algorithm with a Single Individual,” in Proc. IEEE Congress on Evolutionary Computation, Vancouver, Canada, pp. 9172-9179, Jul. 2006.',

 
'J.-H. Kim, K.-H. Lee, Y.-D. Kim and I.-W. Park, “Genetic Representation for Evolvable Artificial Creature,” in Proc. IEEE Congress on Evolutionary Computation, Vancouver, Canada, pp. 6838-6843, Jul. 2006.',

 
'Y.-H. Kim, J.-H. Kim and K.-H. Han, “Quantum-inspired Multiobjective Evolutionary Algorithm for Multiobjective 0/1 Knapsack Problems,” in Proc. IEEE Congress on Evolutionary Computation, Vancouver, Canada, pp. 9151-9156, Jul. 2006.',

 
'Y.-D. Kim, B.-J. Lee, J.-K. Yoo, J.-H. Kim and J.-H. Ryu, “Compensation for the Landing Impact force of a Humanoid Robot by Time Domain Passivity Approach,” in Proc. IEEE International Conference on Robotics and Automation, Orlando, Florida, pp.1225-1230, May. 2006.',

 
'M. Yuchi and J.-H. Kim, “Ecology-inspired Evolutionary Algorithm using Feasibility-based Grouping for Constrained Optimization,” in Proc. IEEE Congress on Evolutionary Computation, Edingurgh, UK, pp. 1455-1461, Sep. 2005.',

 
'J.-S. Jang and J.-H. Kim, “Two-Layered Face Detection System using Evolutionary Algorithm,” in Proc. IEEE Congress on Evolutionary Computation, Edingurgh, UK, pp. 1509-1515, Sep. 2005.',

 
'J.-H. Ryu, B. Hannaford, D.-S. Kwon and J.-H. Kim, “A Simulation/Experimental Study of the Noisy Behavior of the Time Domain Passivity Controller for Haptic Interfaces,” in Proc. IEEE International Conference on Robotics and Automation, Apr. 2005.',

'J.-S. Jang, K.-H. Han and J.-H. Kim, “Face Detection using Quantum-inspired Evolutionary Algorithm,” in Proc. IEEE Congress on Evolutionary Computation, Portland, USA, pp. 2100-2106, Jun. 2004.',

 
'Y.-D. Kim, J.-H. Kim and Y.-J. Kim, “Behavior Selection and Learning for Synthetic Character,” in Proc. IEEE Congress on Evolutionary Computation, Portland, USA, pp. 898-903, Jun. 2004.',

 
'M. Yuchi and J.-H. Kim, “Grouping-based Evolutionary Algorithm: Seeking Balance Between Feasible and Infeasible Individuals of Constrained Optimization Problems,” in Proc. IEEE Congress on Evolutionary Computation, Portland, USA, pp. 280-287, Jun. 2004.',

 
'C.-H. Lee, M. Yuchi and J.-H. Kim, “Two-phase optimization of Fuzzy Controller by Evolutionary Programming,” in Proc. IEEE Congress on Evolutionary Computation, Canberra,Australia, pp. 1949-1957, Dec. 2003.',

 
'K.-H. Lee and J.-H. Kim, “Parallel Evolutionary Optimized Pitching Motion Control for F-16 Aircraft,” in Proc. IEEE Congress on Evolutionary Computation, Canberra, Australia, pp. 1199-1206, Dec. 2003.',

 
'K.-H. Park and J.-H. Kim, “Two mode Q-learning,” in Proc. IEEE Congress on Evolutionary Computation, Canberra, Australia, pp. 2449-2454, Dec. 2003.',

 
'K.-H. Han and J.-H. Kim, “On Setting the Parameters of Quantum-inspired Evolutionary Algorithm for Practical Applications,” in Proc. IEEE Congress on Evolutionary Computation, Canberra, Australia, pp. 178-184, Dec. 2003.',

 
'M. Yuchi and J.-H. Kim, “A Grouping-based Evolutionary Algorithm for Constrained Optimization Problem,” in Proc. IEEE Congress on Evolutionary Computation, Canberra, Australia, pp. 1507-1512, Dec. 2003.',

 
'K.-H. Han, Y.-J. Kim, J.-H. Kim and S. Hsia, “Internet Control of Personal Robot between KAIST and UC Davis,” in Proc. IEEE International Conference on Robotics and Automation, pp. 2184-2189, May. 2002.',

 
'S. Thomas and J.-H. Kim, “Alleviation of Chattering in Variable Structure Co ntrol Signal for Flexible One-link Manipulator,” in Proc. IEEE International Conference on Robotics and Automation, Seoul, Korea, pp. 3847-3852, May. 2001.',

'K.-H. Han, K.-H. Park, C.-H. Lee and J.-H. Kim, “Parallel Quantum-inspired Genetic Algorithm for Combinatorial Optimization Problem,” in Proc. IEEE Congress on Evolutionary Computation, pp. 1422-1429, May. 2001.',

 
'K.-H. Han, S. Kim, Y.-J. Kim, S.-E. Lee and J.-H. Kim, “Implementation of Internet-Based Personal Robot with Internet Control Architecture,” in Proc. IEEE International Conference on Robotics and Automation, pp. 217-222, May. 2001.',

 
'M.-J. Jung and J.-H. Kim, “Fault Tolerant Control Strategy for OmniKity-III,” in Proc. IEEE International Conference on Robotics and Automation, pp. 3370-3375, May. 2001.',

'M.-S. Lee, M.-J. Jung and J.-H. Kim, “Evolutionary Programming-based Fuzzy Logic Path Planner and Follower for Mobile Robots,” in Proc. IEEE Congress on Evolutionary Computation, Jul. 2000.',

'K.-H. Han and J.-H. Kim, “Genetic Quantum Algorithm and its Application to Combinatorial Optimization Problem,” in Proc. IEEE Congress on Evolutionary Computation, pp. 1354-1360, Jul. 2000.',

 
'C.-H. Lee and J.-H. Kim, “Topology and Migration Policy of Fine-grained Parallel Evolutionary Algorithms for Numerical Optimization,” in Proc. IEEE Congress on Evolutionary Computation, Jul. 2000.',

'Y.-J. Kim and J.-H. Kim, “Online Map Building Evolutionary Algorithm for Multi-Agent Mobile Robots with Odometric Uncertainty,” in Proc. IEEE Congress on Evolutionary Computation, Jul. 2000.',

 
'J.-M. Jin and J.-H. Kim, “Omni-directional Mobile Base OK-II,” in Proc. IEEE International Conference on Robotics and Automation, May. 2000.',

'S. Kim and J.-H. Kim, “Q-factor Map Matching Method Using Adaptive Fuzzy Networks,” in Proc. IEEE International Conference on Fuzzy Systems, Seoul, Korea, Aug. 1999.',

'M.-J. Jung, H.-S. Kim, H.-S. Shim and J.-H. Kim, “Fuzzy Rule Extraction for Shooting Action Controller of Soccer Robot,” in Proc. IEEE International Conference on Fuzzy Systems, Seoul, Korea, pp. 556-561, Aug. 1999.',

'J.-H. Kim and B.-K. Kim, “Robot Soccer System for NaroSot,” in Proc. IEEE International Conference on Robotics and Automation, America, May. 1999.',

'M.-J. Jung, H.-S. Shim, H.-S. Kim and J.-H. Kim, “The miniature Omni-directional Mobile Robot OnmiKity-I(OK-I),” in Proc. IEEE International Conference on Robotics and Automation, Detroit, USA, pp. 2686-2691, May. 1999.',

'J.-M. Yang and J.-H. Kim, “A Strategy of Optimal Fault Tolerant Gait for the Hexapod Robot in Crab Walking,” in Proc. IEEE International Conference on Robotics and Automation, Belgium, May. 1998.',

'J.-H. Kim, K.-C. Kim, D.-H. Kim, Y.-J. Kim and P. Vadakkepat, “Path Planning and Role Selection Mechanism for Soccer Robots,” in Proc. IEEE International Conference on Robotics and Automation, Belgium, pp. 3216-3221, May. 1998.',

'J.-M. Yang, I.-H. Choi and J.-H. Kim, “Sliding Mode Control of a Nonholonomic Wheeled Mobile Robot for Trajectory Tracking,” in Proc. IEEE International Conference on Robotics and Automation, Belgium, pp. 2983-2988, May. 1998.',

'J.-M. Yang and J.-H. Kim, “A Strategy of Optimal Fault Tolerant Gait for the Hexapod Robot in Crab Walking,” in Proc. IEEE International Conference on Robotics and Automation, Belgium, pp. 1695-1700, May. 1998.',

'H.-S. Kim, H.-S. Shim, M.-J. Jung and J.-H. Kim, “Action Selection Mechanism for Soccer Robot,” in Proc. IEEE international Symposium on Computaional Intelligence in Robotics and Automation, Monterey, USA, pp. 390-395, Jul. 1997.',

'J.-H. Kim, H.-S.Shim, H.-S.Kim, M.-J. Jung, I.-H.Choi and K.-O.Kim, “Video Proceedings: Building Soccer Robot system for MIROSOT 96,” in Proc. IEEE International Conference on Robotics and Automation, Albuquerque, USA, Apr. 1997.',

'J.-H. Kim, H.-S.Shim, H.-S.Kim, M.-J. Jung, I.-H.Choi and K.-O.Kim, “A Cooperative Multi-agent system and Its Real time application to Robot Soccer,” in Proc. IEEE International Conference on Robotics and Automation, Albuquerque, USA, pp. 638-643, Apr. 1997.',

'J.-M. Yang and J.-H. Kim, “Generation of OPtimal Fault Tolerant Locomotion of the Hexapod Robot over Rough Terrain Using Evolutionary Programming,” in Proc. IEEE Congress on Evolutionary Computation, Indianapolis, USA, pp. 489-494, Apr. 1997.',

'K.-C. Kim, J.-H. Kim, B.-K. Lee and S.-K. Shin, “Multicriteria Fuzzy Expert System for Process Control,” in Proc. IEEE International Conference on Systems, Man and Cybernetics, Oct. 1996.',

'J.-M. Yang and J.-H. Kim, “Fault Tolerant Locomotion Control of the Hexapod Robot,” in Proc. IEEE International Conference on Systems, Man and Cybernetics, Beijing, China, Oct. 1996.',

'S. Kim and J.-H. Kim, “Near-Global Optimal Trajectory Planning of a Redundant Manipulator using Evolutionary Computation,” in Proc. IEEE International Conference on Industrial Electronics, Control, and Instrumentation, Taipei, Taiwan, Aug. 1996.',

'C.-H. Lee and J.-H. Kim, “Evolutionary Ordered Neural Network and Its Application to Robot Manipulator Control,” in Proc. IEEE International Conference on Industrial Electronics, Control, and Instrumentation, Taipei, Taiwan, Aug. 1996.',

'H. Myung and J.-H. Kim, “Constrained Optimization Using Two-Phase Evolutionary Programming,” in Proc. IEEE Congress on Evolutionary Computation, Japan, pp. 262-267, Aug. 1996.',

'S. Kim and J.-H. Kim, “Optimal Trajectory Planning of a Redundant Manipulator Using Evolutionary Programming,” in Proc. IEEE Congress on Evolutionary Computation, Aug. 1996.',

'J.-Y. Jeong, H.-K. Chae, S.-W. Lee and J.-H. Kim, “Low Velocity Friction Identification and Compensation of PD Using Accelerated Evolutionary Programming,” in Proc. IEEE International Conference on Evolutionary Computation, Aug. 1996.',

'C.-H. Lee and J.-H. Kim, “Evolutionary Ordered Neural Network with a linked-list Encoding Scheme,” in Proc. IEEE Congress on Evolutionary Computation, Aug. 1996.',

'J.-M. Yang and J.-H. Kim, “Optimization of Discrete Event Systems Using Evolutionary Programming,” in Proc. IEEE Congress on Evolutionary Computation, Aug. 1996.',

'A.-V. Topalov, K.-C. Kim, J.-H. Kim and B.-K. Lee, “Fast Genetic On-Line Learing Algorithm for Neural Network and Its Application to Temperature Control,” in Proc. IEEE Congress on Evolutionary Computation, Nagoya, Japan, May. 1996.',

'J.-Y. Jeon, J.-H. Kim and K. Koh, “High Precision Control of X-Y Table using Experimental Evolutionary Programming Based-scheme,” in Proc. IEEE International Conference on Robotics and Automation, Apr. 1996.',

'H.-S. Shim and J.-H. Kim, “Robust control of non-holonomic wheeled mobile robot based on evolutionary programming for optimal motion,” in Proc. IEEE Congress on Evolutionary Computation, Australia, pp. 625-630, Nov. 1995.',

'J.-H. Kim, J.-Y. Jeon, H.-K. Chae and K.-I Koh, “A novel evolutionary algorithm with fast convergence,” in Proc. IEEE Congress on Evolutionary Computation, Australia, pp. 228-238, Nov. 1995.',

'J.-M. Yang and J.-H. Kim, “On the Organization Level Structure of the Hierarchical Intelligent Machine,” in Proc. IEEE International Conference on Robotics and Automation, Nagoya, Japan, May. 1995.',

'H.-S. Shim, J.-H. Kim and K.-I. Koh, “Variable Structure Control of Nonholonomic Wheeled Mobile Robot,” in Proc. IEEE International Conference on Robotics and Automation, Nagoya, Japan, May. 1995.',

'H.-S. Shim and J.-H. Kim, “Robust Adaptive Control of Nonholonomic Wheeled Mobile Robot,” in Proc. IEEE ICIT, Kwang Ju, China, Dec. 1994.',

'H. Myeong and J.-H. Kim, “Time-Varying Two-Phase Optimization for Neural Network Learning,” in Proc. IEEE World Congress on Computational Intelligence, Orlando, Florida, Jun. 1994.',

'K.-Ch. Kim and J.-H. Kim, “Multicriteria Fuzzy Control and Its Application to DC Servomotor Position control,” in Proc. IEEE World Congress on Computational Intelligence, Orlando, Florida, Jun. 1994.',
 
'J.-Y. Jeon and J.-H. Kim, “Generalized Predictive Control using Fuzzy Neural Network Model,” in Proc. IEEE World Congress on Computational Intelligence, Orlando, Florida, Jun. 1994.',

'S.-W. Lee and J.-H. Kim, “Control of Systems with Deadzones Using Neural Network Based Learning Controller,” in Proc. IEEE World Congress on Computational Intelligence, Orlando, Florida, Jun. 1994.',

'J.-H. Kim, S.-W. Lee, K.-Ch. Kim and Edwin K.P.Chong, “Fuzzy Precompensated PID Controller,” in Proc. Second IEEE Conference on Control Applications, Canada, Sep. 1993.',

'J.-H. Kim, S.-W. Lee and J. H. Kim, “Lyapunov Redesign for Direct Adaptive Control of Nonminimum Phase Systems,” in Proc. IEEE 30th CDC, Brighton, U.K., Dec. 1991.',

'J.-H. Kim and D.-J. Park, “A Discrete Adaptive Observer with Exponential Data Weighting,” in Proc. IEEE 29th CDC, Hawaii, U.S.A., Dec. 1990.',

'Joon-Hyuk Kim, Gyeong-Moon Park and and Jong-Hwan Kim, “Multi-channel Classification Resonance Network,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, Korea, Nov. 2019.',

'Jin-Tae Kim, Young-Min Kim, Natnael Shewangizaw Zewge and Jong-Hwan Kim, “A Robust Client-Server Architecture for Map Information Processing and Transmission for Distributed Visual SLAM,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, Korea, Nov. 2019.',

'Natnael Shewangizaw Zewge, Young-Min Kim, Jin-Tae Kim and Jong-Hwan Kim, “Millimeter-Wave Radar and RGB-D Camera Sensor Fusion for Real-Time People Detection and Tracking,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, Korea, Nov. 2019.',

'Sun-Kyung Lee and Jong-Hwan Kim, “BALD-VAE: Generative Active Learning Based on the Uncertainties of Both Labeled and Unlabeled Data,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Daejeon, Korea, Nov. 2019.',

'Won-Hyon Lee, Sahng-Min Yoo, Jae-Woo Choi and Ue-Hwan Kim and Jong-, “Human Robot Social Interaction Framework based on Emotional Episodic Memory,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Putrajaya, Malaysia, Dec. 2018.',

'Bum-Soo Yoo and Jong-Hwan Kim, “Gaze Control of Humanoid Robot for Learning from Demonstration,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Bucheon, Korea, Dec. 2015.',


'Ue-Hwan Kim and Jong-Hwan Kim, “A Color Constancy Algorithm using Photodetector Characteristics of a Camera for Indoor Scenes,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Bucheon, Korea, Dec. 2015.',

 
'Chan Woo Park, Jong-Hyeon Seon, Jung-Hoon Kim and Jong-Hwan Kim, “Pet Care Robot for Playing with Canines,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Bucheon, Korea, Dec. 2015.',

 
'You-Min Lee and Jong-Hwan Kim, “Trajectory Generation Using RNN with Context Information for Mobile Robots,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Bucheon, Korea, Dec. 2015.',

 
'Bum-Soo Yoo, Yong-Ho Yoo, Woo-Ri Ko, Seung-Jae Lee, Seung-Hwan Baek, Se-Hyoung Cho and Jong-Hwan Kim, “Realization of Task Intelligence Based on the Intelligence Operating Architecture for Assistive Robots,” in Proc. International Conference on Artificial Intelligence (ICAI), Las Vegas, U.S.A., Jul. 2015.',

 
'Gyeong-Moon Park, Yong-Ho Yoo and Jong-Hwan Kim, “REM-ART: Reward-based Electromagnetic Adaptive Resonance Theory,” in Proc. International Conference on Artificial Intelligence (ICAI), Las Vegas, U.S.A., Jul. 2015.',

 
'Seung-Jae Lee, Seung-Hwan Baek and Jong-Hwan Kim, “Arm Trajectory Generation based on RRT* for Humanoid Robot,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'Si-Jung Ryu and Jong-Hwan Kim, “Dual Multiobjective Quantum-inspired Evolutionary Algorithm for a Sensor Arrangement in a 2D Environment,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'Deok-Hwa Kim, Seungbeom Han and Jong-Hwan Kim, “Visual Odometry Algorithm Using an RGB-D Sensor and IMU in a Highly Dynamic Environment,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'In-Bae Jeong, Seung-Jae Lee and Jong-Hwan Kim, “RRT*-Quick : A Motion Planning Algorithm with Faster Convergence Rate,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'Bum-Soo Yoo and Jong-Hwan Kim, “Gaze Control Factors for Natural Human Robot Interaction from Scanpath Comparisons,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'Gyeong-Moon Park, Seung-Hwan Baek and Jong-Hwan Kim, “Falling Prevention System from External Disturbances for Humanoid Robots,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'Young-Min Kim and Jong-Hwan Kim, “Modifiable Walking Pattern Generator on Unknown Uneven Terrain,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'You-Min Lee and Jong-Hwan Kim, “Robust and Reliable Feature Extraction Training by Using Unsupervised Pre-training with Self-Organization Map,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'Yong-Ho Yoo and Jong-Hwan Kim, “Robust Object Recognition Under Partial Occlusions Using an RGB-D camera,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'Woo-Ri Ko and Jong-Hwan Kim, “Behavior Selection Method of Humanoid Robots to Perform Complex Tasks,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'Ji-Hyeong Han and Jong-Hwan Kim, “3D Visibility Check in Webots for Human Perspective Taking in Human-Robot Interaction,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'Woo-Young Go and Jong-Hwan Kim, “Wireless Remote Control of Robot Dual Arms and Hands Using Inertial Measurement Units for Learning from Demonstration,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'Chang-Soo Park and Jong-Hwan Kim, “Stable Modifiable Walking Pattern Generator with a Vertical Foot Motion by Evolutionary Optimized Central Pattern Generator,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Beijing, China, Nov. 2014.',

 
'Si-Jung Ryu, Jong-Hwan Kim and Ki-Baek Lee, “DMQEA: Dual Multiobjective Quantum-inspired Evolutionary Algorithm,” in. Proc. International Conference on Evolutionary Computation Theory and Applications, Rome, Italy, Oct. 2014.',

 
'Woo-Ri Ko and Jong-Hwan Kim, “Organization and Selection Methods of Composite Behaviors for Artificial Creatures Using the Degree of Consideration-based Mechanism of Thought,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Denver, USA,, Dec. 2013.',

 
'Si-Jung Ryu and Jong-Hwan Kim, “An Evolutionary Feature Selection Algorithm for Classification of Human Activities,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Denver, U.S.A., Dec. 2013.',

 
'Deok-Hwa Kim and Jong-Hwan KIm, “Visual Loop-Closure Detection Method Using Average Feature Descriptors,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Denver, USA,, Dec. 2013.',

 
'Woo-Young Go and Jong-Hwan Kim, “Flexible and Wearable Hand Exoskeleton and Its Application to Computer Mouse,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Denver, U.S.A., Dec. 2013.',

 
'C.-S. Park and J.-H. Kim, “Stable Modifiable Walking Pattern Generator with Arm Swing Motion Using Evolutionary Optimized Central Pattern Generator,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Denver, USA,, Dec. 2013.',

 
'Yong-Ho Yoo and Jong-Hwan Kim, “Target-driven Visual Words Representation via Conditional Random Field and Sparse Coding,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Denver, U.S.A., Dec. 2013.',

 
'Bum-Soo Yoo and Jong-Hwan Kim, “Scanpath Analysis with Fixation Maps to Provide Factors for Natural Gaze Control,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Denver, USA,, Dec. 2013.',

 
'Ji-Hyeong Han and Jong-Hwan Kim, “Consideration about the Application of Dynamic Time Warping to Human Hands Behavior Recognition for Human-Robot Interaction,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Denver, U.S.A., Dec. 2013.,'

 
'Seung-Jae Lee, Chang-Young Jung, Bum-Soo Yoo, Se-Hyoung Cho and Young-Min Kim and Jong-Hwan Kim, “Arm Gesture Generation of Humanoid Robot Mybot-KSR for Human Robot Interaction,” in Proc. 2013 FIRA Robot World Congress, Kuala Lumpur, Malaysia, Aug. 2013.',

 
'Deok-Hwa Kim, Yong-Ho Yoo, Si-Jung Ryu, Woo-Young Go and Jong-Hwan Kim, “Automatic Color Detection for MiroSOT Using Quantum-inspired Evolutionary Algorithm,” in Proc. 2013 FIRA Robot World Congress, Kuala Lumpur, Malaysia, Aug. 2013.',

 
'Ji-Hyeong Han and Jong-Hwan Kim, “Human Intention Reading by Fuzzy Cognitive Map: A Human-Robot Cooperative Object Carrying Task,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea, Dec. 2012.',

 
'Young-Dae Hong and Jong-Hwan Kim, “Walking Pattern Generation on Inclined and Uneven Terrains for Humanoid Robots,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Dec. 2012.',

 
'Si-Jung Ryu and Jong-Hwan Kim, “Distributed Multiobjective Quantum-inspired Evolutionary Algorithm (DMQEA),” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea, Dec. 2012.',

 
'Deok-Hwa Kim and Jong-Hwan Kim, “Image-based ICP Algorithm for Visual Odometry Using an RGB-D Sensor in a Dynamic Environment,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea, Dec. 2012.',

 
'Yong-Ho Yoo and Jong-Hwan Kim, “Mathematical Formula Recognition based on Modified Recursive Projection Profile Cutting and Labeling with Double Linked List,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea, Dec. 2012.',

 
'Seung-beom Han, Jeong-Ki Yoo and Jong-Hwan Kim, “Obstacle Detection Using Fuzzy Integral-Based Gaze Control for Mobile Robot,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea, Dec. 2012.',

 
'Jeong-Ki Yoo, Seung-Beom Han, Jong-Hwan Kim and , “Sway Motion Cancellation Scheme Using a RGB-D Camera-based Vision System for Humanoid Robots,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea, Dec. 2012.',

 
'C.-S. Park and J.-H. Kim, “Stable Modifiable Walking Pattern Algorithm with Constrained Optimized Central Pattern Generator,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea,, Dec. 2012.',

 
'Sheir Afgen Zaheer and Jong-Hwan Kim, “Context-aware Decision Making for Maze Solving,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea, Dec. 2012.',

 
'Dong-Hyun Lee, Ji-Hyeong Han and Jong-Hwan Kim, “Market-based Multiagent Framework for Balanced Task Allocation,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea, Dec. 2012.',

 
'Ki-Baek Lee and Jong-Hwan Kim, “A Homogeneous Distributed Computing Framework for Multi-Objective Evolutionary Algorithm,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea, Dec. 2012.',

 
'Woo-Ri Ko and Jong-Hwan Kim, “Behavior Selection Method for Entertainment Robots Using Intelligence Operating Architecture,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea,, Dec. 2012.',

 
'Seung-Jae Lee and Jong-Hwan Kim, “Development of a Quadrocoptor Robot with Vision and Ultrasonic Sensors for Distance Sensing and Mapping,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea, Dec. 2012.',

 
'Chang-Young Jung and Jong-Hwan Kim, “Real-time Trajectory Generation for Both Arms of a Humanoid Robot,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea,, Dec. 2012.',

 
'Seung-Hwan Choi and Woo-Ri Ko and Jong-Hwan Kim, “Episodic Memory Design for Predicting the User’s Intention,” in Proc. International Conference on Robot Intelligence Technology and Applications (RiTA), Gwangju, Korea,, Dec. 2012.',

 
'Si-Jung Ryu, Ki-Baek Lee, Bum-Soo Yoo, Tae-Jin Kim, Seung-Jae Lee and Jong-Hwan Kim, “Multiobjective Quantum-Inspired Evolutionary Algorithm with Preference-Based Selection 2: Comparison Study,” in Proc. FIRA-TAROS 2012, Bristol, U.K., Aug. 2012.',

 
'Woo-Ri Ko, Chang-Young Jung, Yong-Ho Yoo, Deok-Hwa Kim and Jong-Hwan Kim, “Behavior Selection Algorithm for Personal Service Robots Using Intelligence Operating Architecture,” in Proc. FIRA-TAROS 2012, Bristol, U.K., Aug. 2012.',

 
'Bum-Soo Yoo and Se-Hyoung Cho and Jong-Hwan Kim, “Facial Expression Generation Using Fuzzy Integral for Robotic Heads,” in Proc. FIRA Robot World Congress, Kaohsiung, Taiwan, Aug. 2011.',

 
'Si-Jung Ryu and Jong-Hwan Kim, “Motion Recognition in Wearable Sensor System Using an Ensemble Artificial Neuro-Molecular System,” in Proc. FIRA Robot World Congress, Kaohsiung, Taiwan, Aug. 2011.',

 
'S.-H. Choi, J.-H. Han and J.-H. Kim, “3D-Position Estimation for Hand Gesture Interface Using a Single Camera,” Human-Computer Interaction International 2011, Orlando, USA, Jul. 2011.',

 
'Dong-Hyun Lee, Ki-In Na and Jong-Hwan Kim, “Task and Role Selection Strategy for Multi-robot Cooperation in Robot Soccer,” in Proc. FIRA Robot World Congress, India,, Sep. 2010.',

 
'C.-S. Park, J.-K. Yoo, Y.-D. Hong, K.i-B. Lee, S.-J. Ryu and J.-H. Kim, “Walking Pattern Generator Using an Evolutionary Central Pattern Generator,” in Proc. FIRA Robot World Congress, India, Sep. 2010.',

 
'S.-H. Choi, S.-B. Han and J.-H. Kim, “Soty-Segment: Robust Color Patch Design to Lighting Condition Variation,” in Proc. FIRA RoboWorld Congress 2009, Incheon, Korea, pp. 300-309, Aug. 2009.',

 
'D.-H. Lee and J.-H. Kim, “Motivation and Context-Based Multi-Robot Architecture for Dynamic Task, Role and Behavior Selections,” in Proc. FIRA RoboWorld Congress 2009, Incheon, Korea, pp. 161-170, Aug. 2009.',

 
'Y.-D. Hong and J.-H. Kim, “Footstep Planning Based on Univector Field Method for Humanoid Robot,” in Proc. the FIRA RoboWorld Congress 2009 on Advances in Robotics, LNCS 5744, Incheon, Korea, Aug. 2009.',

 
'D.-H. Lee, J.-S. Sun, S.-B. Han, C.-S. Park and J.-H. Kim, “Omnidirectional Robot System and Localization for FIRA ROBOSOT,” in Proc. 2008 FIRA Robot World Congress, Qingdao, China, Jul. 2008.',

 
'Jeong-Ki Yoo, Bum-Joo Lee and Jong-Hwan Kim, “Vision Simulator of HSR-VII for Obstaclerun in HuroCup,” in Proc. CIRAS, Linz, Austria, Jul. 2008.',

 
'J.-K. Yoo, Y.-D. Kim, B.-J. Lee, I.-W. Park and J.-H. Kim, “Humanoid Robot System, HanSaRam-VII for RoboMarathon in HuroCup,” in Proc. 17th World Congress The International Federation of Automatic Control, Seoul, Korea, Jul. 2008.',


'S.-H. Choi, S.-B. Han and J.-H. Kim, “Interactive Genetic Algorithm for Designing the Appearance of Software Robot using Homologous Chromosome Representation,” in Proc. 17th World Congress The International Federation of Automatic Control, Seoul, Korea, pp. 9151-9155, Jul. 2008.',

 
'Y.-S. Lim, S.-H. Choi, J.-H. Kim and D.-H. Kim, “Evolutionary Univector Field-based Navigation with Collision Avoidance for Mobile Robot,” in Proc. 17th World Congress The International Federation of Automatic Control, Seoul, Korea, pp. 12787-12792, Jul. 2008.',

 
'S.-L. Choi and J.-H. Kim, “Reducing Effect of Outliers in Landmark-based Spatial Localization using MLESAC,” in Proc. 17th World Congress The International Federation of Automatic Control,, Seoul, Korea, Jul. 2008.',

 
'D.-H. Kim and J.-H. Kim, “CSMA/CD-R for aWireless Multi-robot Commuication,” in Proc. 17th World Congress The International Federation of Automatic Control, Seoul, Korea, Jul. 2007.',

'N.S. Kuppuswamy, S.-H Cho, D. Stonier, S.-L. Choi and J.-H Kim, “Design of an Omnidirectional Robot for FIRA ROBOSOT,” in Proc. 12th FIRA Robot World Congress, San Francisco, USA, Jun. 2007, Jun. 2007.',

 
'J.-K. Yoo, Y.-D. Kim, B.-J. Lee, I.-W. Park, N. S. Kuppuswamy and J.-H. Kim, “Hybrid Architecture for Kick Motion of Small-sized Humanoid Robot, HanSaRam-VI,” in Proc. SICE-ICASE International Joint Conference, pp. 1174-1179, Oct. 2006.',

 
'N. S. Kuppuswamy, S.-H. Cho and J.-H. Kim, “A Cognitive Control Architecture for an Artificial Creature using Episodic Memory,” in Proc. SICE-ICASE International Joint Conference, Busan, Korea, pp. 3104-3110, Oct. 2006.',

'Y.-D. Kim, B.-J. Lee, S.-H. Choi, I.-W. Park and J.-H. Kim, “Humanoid Robot HanSaRam: Recent Development and Compensation for the Landing Impact Force by Time Domain Passivity Approach,” in Proc. 2005 FIRA Robot World Congress, Singapore, Dec. 2005.',

'J.-H. Ryu and J.-H. Kim, “Stable and High Performance Teleoperation with Time Domain Passivity Control: Reference Energy Following Scheme,” in Proc. Int. Conf. on Advanced Robotics, Seattle, USA, Jul. 2005.',

'B.-J. Lee, Y.-D. Kim and J.-H. Kim, “Balance Control of Humanoid Robot for Hurosot,” in Proc. IFAC World Congress, Prague, Czech, Jul. 2005.',

'J.-H. Ryu and J.-H. Kim, “Time Domain Passivity Approach for Soft and Deformable Environments,” in Proc. Int. Conf. on Control, Automation and Systems, Ilsan KINTEX, Korea, Jun. 2005.',

'J.-H. Kim, K.-H. Lee and Y.-D. Kim, “Ubiquitous Robot: The 3rd Generation of Robotics (Plenary speech),” in Proc. the 2nd International Symposium on Mechatronics, Sharjah, United Arab Emirates, Apr. 2005.',

'Y.-D. Kim, B.-J. Lee, J.-K. Yoo, S.-H. Choi and J.-H. Kim, “Humanoid Robot Hansaram: Yawing Moment Cancellation and ZMP Compensation,” in Proc. AUS International Symposium on Mechatronics, Sharjah, United Arab Emirates, Apr. 2005.',

 
'J.-H. Kim, K.-H. Lee, Y.-D. Kim, B.-J. Lee and J.-K. Yoo, “The Origin of Artificial Species: Humanoid Robot HanSaRam (Plenary Speech Paper),” in Proc. 2nd International Conference on HNICEM05, Manila, Philippines, Mar. 2005.',

'J.-H. Kim, Y.-D. Kim and K.-H. Lee, “The Third Generation of Robotics: Ubiquitous Robot,” in Proc. the International Conference on Autonomous, Palmerston North, New Zealand, Dec. 2004.',

 
'K.-H. Park, J. Jo and J.-H. Kim, “Stabilization of Biped Robot based on Two mode Q-learning,” in Proc. International Conference on Autonomous Robots and Agents, Palmerston North, New Zealand, Dec. 2004.',

'J.-H. Park, J.-H. Kim and B.-H. Ahn, “Evolutionary Learning for Fuzzy Path Planning of Shooting Acion for Robot Soccer,” in Proc. The 5th Internaltional Conference on SimulatedEvolution And Learning, Oct. 2004.',

'B.-J. Lee, Y.-D. Kim and J.-H. Kim, “Balance Control of Humanoid Robot using its Upper Body,” in Proc. 2004 FIRA Robot World Congress, Oct. 2004.',

'M.-H. Koo, Y.-K. Lee, K.-H. Lee, T.-H. Kim, J.-K. Lee and J.-H. Kim, “Development of Robot Soccer System for 11-A-Side MiroSot,” in Proc. 2004 FIRA Robot World Congress, Oct. 2004.',

'K.-H. Lee and J.-H. Kim, “A Survey of Ubiquitous Space Where Ubiquitous Robots will Exist,” in Proc. 2004 FIRA Robot World Congress, Oct. 2004.',

'M. Yuchi and J.-H. Kim, “Grouping-Based Evolutionary Algorithm Improves The Performance of Dynamic Penalty Method for Constrained Optimization Problems,” in Proc. The 5th Internaltional Conference on SimulatedEvolution And Learning, Oct. 2004.',

'J.-H. Kim, “Ubiquitous Robot (Keynote Speech Paper),” in Proc. Fuzzy Days International Conference, Dortmund, Germany, Sep. 2004.',

'J.-H. Kim, K.-H. Park, J.-S. Jang, Yong-Duk Kim, Bum-Joo Lee and Ki-Pyo Kim, “Humanoid Robot HanSaRam: Schemes for ZMP compensation,” in Proc. Int. Conf. on Computational Intelligence, Robotics and Autonomous Systems(CIRAS), Singapore, Dec. 2003.',

'K.-H. Park and J.-H. Kim, “Q-learning Algorithms for Soccer Robot,” in Proc. FIRA Robot World Congress, Vienna, Austria, Sep. 2003.',

'J.-S. Jang, K.-H. Han and J.-H. Kim, “Quantum-Inspired Evolutionary Algorithm-Based Face Verification,” in Proc. Genetic and Evolutionary Computation Conference – GECCO, Chicago, USA, Jul. 2003.',

'C.-H. Lee, M. Yuchi, H. Myung and J.-H. Kim, “The Principle of Maximum Entropy-Based Two-Phase Optimization ofFuzzy Controller by Evolutionary Programming,” in Proc. Genetic and Evolutionary Computation Conference – GECCO, Chicago, USA, pp. 638 – 639, Jul. 2003.',

 
'K.-H. Han and J.-H. Kim, “On Setting the Parameters of QEA for Practical Applications: Some Guidelines Based on Empirical Evidence,” in Proc. Genetic and Evolutionary Computation Conference – GECCO, Chicago, USA, pp. 427 – 428, Jul. 2003.',

'J.-H. Kim, D.-H. Kim, Y.-J. Kim, K.-H. Park, J.-H. Park, Ch.-K. Moon, K. -T. Seow and K.-C. Koh, “Humanoid Robot HanSaRam: Recent Progress and Development,” in Proc. the Int. Conf. on Humanoid, Nanotechnology, Information technology, Communication and control, Environment, and Management, pp. 27-30, May. 2003.',

'J.-S. Jang, M.-J. Jung, J.-H. Kim and Jong-Suk Choi, “Cooperative localization in Multi-agent Robotic System,” in Proc. the 2002 FIRA Robot World Congress, May. 2002.',

'K.-H. Han, K.-H. Lee, C.-K. Moon, H.-B. Lee and J.-H. Kim, “Robot Soccer System of SOTY 5 for Middle League MiroSot,” in Proc. the 2002 FIRA Robot World Congress, pp. 632-635, May. 2002.',

'K.-H. Han and J.-H. Kim, “Introduction of Quantum-inspired Evolutionary Algorithm,” in Proc. the 2002 FIRA Robot World Congress, pp. 243-248, May. 2002.',

'K.-H. Han and J.-H. Kim, “Direct Internet Control Architecture for Personal Robot,” in Proc. the 2002 FIRA Robot World Congress, pp. 264-268, May. 2002.',

'D.-H. Kim, J.-H.Park and J.-H. Kim, “Limit-cycle Navigation Method for Soccer Robot,” in Proc. Int. Conf. on Computational Intelligence, Robotics and Autonomous Systems(CIRAS), Singapore, Nov. 2001.',

'S. Thomas and J.-H. Kim, “On Alleviation of Chattering in Variable Structure Model Following Control Signal for Flexible Manipulator,” in Proc. the 4th Asian Conference on Robotics and its Applications (ACRA 2001) at the Robotics and Mechatronics Congress 2001, Singapore, Jun. 2001.',

'K.-H. Han and J.-H. Kim, “Analysis of Quantum-inspired Evolutionary Algorithm,” in Proc. the 2001 International Conference on Artificial Intelligence, CSREA Press, Vol. 2, pp. 727-730, Jun. 2001.',

'J.-H. Kim, K.-H. Han, S. Kim and Y.-J. Kim, “Internet-Based Personal Robot System using Map-Based Localization,” in Proc. the 32nd International Symposium on Robotics, pp. 1282-1287, Apr. 2001.',

'H.-S. Kim and J.-H. Kim, “Circle detection algorithm using pairs of the intersecting chords,” in Proc. Int. symposium on robotics and automation, Monterrey, Mexico, Oct. 2000.',

'M.-J. Jung and J.-H. Kim, “Omni-directional Wheeled Mobile Robot OmniKity,” in Proc. World Automation Congress, Hwaii, USA, Jun. 2000.',

'H.-S. Shim, M.-J. Jung, H.-S. Kim, J.-H. Kim and P. Vadakkepat, “Role level design in a hybrid control structure for a vision-based soccer robot system,” in Proc. AROB 4th 99, Oita University, Oita, Japan, Jan. 1999.',

'Y.-J. Kim, D.-H. Kim and J.-H. Kim, “Evolutionary Programming-Based Vector Field Method for Fast Mobile Robot Navigation,” in Proc. SEAL 98, Serial. 3, Canberra, Australia, pp. 198-205, Nov. 1998.',

'H. Myung and J.-H. Kim, “Multiple Largrange Multiplier Method for Constrained Evolutionary Optimization,” in Proc. SEAL 98, Serial. 3, Canberra, Australia, pp. 1-9, Nov. 1998.',

'S. Kim, J.-H. Kim and I.-H. Hyun, “Development of a Map Matching Algorithm for Car Navigation System using Fuzzy Q-factor Algorithm,” in Proc. World Congress on Intelligent Transport Systems, Serial. 5, Seoul, Korea, pp. 1503-1511, Oct. 1998.',

'C.-H. Lee and J.-H. Kim, “Measurement of Machine Intelligence of Surface Mounting Machine using Choquet Integral,” in Proc. World Automation Congress, Anchorage, USA, pp. 621-626, May. 1998.',

'J.-M. Yang and J.-H. Kim, “Controller Design for Nonholonomic Wheeled Mobile Robots Using Theory of Variable Structure Systems,” in Proc. World Automation Congress, Anchorage, USA, pp. 5-10, May. 1998.',

'H. Myung and J.-H. Kim, “SMD Production Optimization Using Evolutionary Computation,” in Proc. World Automation Congress (WAC 98), Anchorage, USA, Apr. 1998.',

'H. Myung and J.-H. Kim, “Hybrid Interior-Lagrangian Penalty based Evolutionary Computation,” in Proc. Annual Evolutionary Programming Conf., Serial. 7, San Diego, USA, Mar. 1998.',

'J.-H. Kim, H.-S. Shim, H.-S. Kim, M.-J. Jung and P. Vadakkepat, “Miro-Robot Soccer System : Action Selection Mechanism and Strategies,” in Proc. Third ECPD International Conference on Advanced Robotics, Intelligent Automation and Active Systems, Bremen, Germany, Sep. 1997.',

'J.-M. Yang and J.-H. Kim, “Tracking Control of Wheeled Mobile Robots Using Variable Structure Systems,” in Proc. 2nd Asian Control Conference, Serial. 2, Seoul, Korea, pp. 381-384, Jul. 1997.',

'Spripada S, Prahlad V, K.-C. Kim and J.-H. Kim, “Multi-Agent Centralized Control in Soccer Robots,” in Proc. Micro-Robot World Cup Soccer Tournament, Serial. 2, Dae-jeon, Korea, pp. 49-54, Jun. 1997.',

'H.-S.Shim, M.-J.Jung, H.-S.Kim, I.-H.Choi and J.-H. Kim, “Development of Vision-Based Soccer Robot System for Multi-agent Cooperative Systems,” in Proc. Micro-Robot World Cup Soccer Tournament, Serial. 2, Dae-jeon, Korea, pp. 29-36, Jun. 1997.',

'H. Myung and J.-H. Kim, “Evolian:Evolutionary Optimization based on Lagrangian with constraint scaling,” in Proc. The 6th International Conference on Evolutionary Programming, Serial. 6, Indianapolis, USA, pp. 177-188, Apr. 1997.',

'H. Myung and J.-H. Kim, “Two Phase Evolutionary Programming for Constrained Numerical Optimization,” in Proc. the 35th Conf. on Decision and Control, Japan, Dec. 1996.',

'J.-H. Kim, J.-Y. Jeon, S.-W. Lee and K. Koh, “High Precision Control of Positioning Systems with Nonsmooth Nonlinearity,” in Proc. the 35th Conf. on Decision and Control, Japan, Dec. 1996.',

'J.-M. Yang and J.-H. Kim, “Control and Optimization of Cost-Evaluated Discrete Event Systems,” in Proc. Int. Conf. on Decision and Control, Japan, Dec. 1996.',

'H. Myung and J.-H. Kim, “Lagrangian Based Evolutionary Programming for Constrained Optimization,” in Proc. Int. Conf. on Simulated and Learning, Oct. 1996.',

'H.-S. Shim, M.-J. Jung, H.-S. Kim, I.-H. Choi, W.-S. Han and J.-H. Kim, “Designing Distributed Control Architecture for Cooperative Multiagent System,” in Proc. 1st Micro-robot Worldcup Soccer Tournament, Oct. 1996.',

'H.-S. Kim and J.-H. Kim, “Improving Global Optimization by Modified Mutation Operator,” in Proc. Asia-Pacific Conf. on Simulated Evolution and Learning, Oct. 1996.',

'C.-H. Lee and J.-H. Kim, “The Identification of Nonlinear Systems Using EONNs,” in Proc. Int. Conf. on Simulated and Learning, Aug. 1996.',

'S.-W. Lee and J.-H. Kim, “Robust Adaptive Friction Compensation Using a Fuzzy Neural Network,” in Proc. Int. Symposium on Intelligent Automation and Control, France, May. 1996.',

'H. Myung and J.-H. Kim, “Frequency Modulation Neural Network Model and Its Learning Algorithm,” in Proc. KFIS Spring Conf, Vol. 6, No. 1, Mar. 1996.',

'H. Myung and J.-H. Kim, “Two-Phase Evolutionary Programming Scheme for Constrained Optimization,” in Proc. KFIS Spring Conf, Vol. 6, No. 1, Mar. 1996.',

'J.-H. Kim and H. Myung, “A Two Phase Evolutionary Programming for General Constranied Optimization Problem,” in Proc. Int. Conf. on Evolutionary Programming, Serial. 5, Feb. 1996.',

'J.-H. Kim and J.-Y. Jeon, “Evolutionary Programing-based High-Precision controller Design,” in Proc. Int. Conf. on Evolutionary Programming, Feb. 1996.',

'J.-H. Kim, M.-J. Jung, H.-S. Shim and S.-W. Lee, “Autonomous Micro-Robot ‘Kity’ for Maze Contest,” in Proc. Int. symposium on Artificial Life and Robotics, Japan, pp. 261-264, Feb. 1996.',

'J.-H. Kim and H. Myung, “A Two-Phase Evolutionary Programming for General Constrained Optimization Problem,” in Proc. the Fifth Annual Conf. on Evolutionary Programming, Feb. 1996.',

'J.-H. Kim and J.-Y. Jeon, “Evolutionary Programming-Based High-Precision Controller Design,” in Proc. the Fifth Annual Conf. on Evolutionary Programming, Feb. 1996.',

'J.-H. Kim, M.-M. Yang, H.-S. Shim and S.-W. Lee, “Autonomous Micro-Robot ‘Kity’ for Maze Contest,” in Proc. Intl. Symp. on Artificial Life and Robotics, Japan, Feb. 1996.',

'K.-M. Koo and J.-H. Kim, “CMAC Network-Based Robust Controller for Systems with Friction,” in Proc. Int. Conf. on Decision and Control, Dec. 1995.',

'H. Myung and J.-H. Kim, “Solving Heavily Constrained Problems Using Hybrid Evolutionary Optimization,” in Proc. Australian Joint Conference on AI, Serial. 8, Australia, pp. 587 – 595, Nov. 1995.',

'K.-Ch. Kim and J.-H. Kim, “Evolutionary programming based multicriteria fuzzy expert system,” in Proc. Australian Joint Conference on AI, Serial. 8, Australia, pp. 475 – 482, Nov. 1995.',

'H. Myung and J.-H. Kim, “Constrained optimization using a two-phase evolutionary programming,” in Proc. Korea-Australia Joint Workshop on EC, Serial. 1, Korea, pp. 258 – 269, Sep. 1995.',

'J.-H. Kim, H. Myung and J.-Y. Jeon, “Hybrid evolutionary scheme with fast convergence for constrained optimization problems,” in Proc. Korea-Australia Joint Workshop on EC, Serial. 1, Korea, pp. 246 – 257, Sep. 1995.',

'H.-Sh. Shim and J.-H. Kim, “Robust Control of Non-holonomic Wheeled Mobile Robot Based on Evolutionary Programming for Optimal Locomotion,” in Proc. Korea-Australia Joint Workshop on EC, Serial. 1, Korea, pp. 206 – 216, Sep. 1995.',

'J.-Y. Jeon and J.-H. Kim, “High Precision Controller Design Using EP,” in Proc. Korea-Australia Joint Workshop on EC, Serial. 1, Korea, pp. 119 – 127, Sep. 1995.',

'K.-Ch. Kim and J.-H. Kim, “Evolutionary Programming Based Multicriteria Fuzzy Expert System,” in Proc. Korea-Australia Joint Workshop on EC, Serial. 1, Tae-jeon, Korea, pp. 58 – 76, Sep. 1995.',

'J.-H. Kim, H.-K. Chae, J.-Y. Jeon and S.-W. Lee, “Friction Parameter Identification and Compensation Scheme of X-Y Table by Using Evolutionary Algorithm,” in Proc. 95 SICICI, Singapore, Jul. 1995.',

'J.-H. Kim and H. Myung, “Fuzzy Logic Control Using Evolutionary Programming and Principle of Maximum Entropy,” in Proc. First Int. Symposium on Fuzzy Logic, Switzerland, May. 1995.',

'J.-H. Kim and S.-W. Lee, “Robust Adaptive Compensation Using Fuzzy Neural Network,” in Proc. First Int. Symposium on Fuzzy Logic, Switzerland, May. 1995.',

'J.-Y. Jeon, J.-H. Kim and K.-I. Koh, “Evolutionary Programming Based Fuzzy Precompensation of PD Controllers for Systems with Deadzones and Saturations,” in Proc. First Int. Symposium on Fuzzy Logic, Switzerland, May. 1995.',

'H. Myung, J.-H. Kim and David B. Fogel, “Preliminary Investigation into a Two-Stage Method of Eovolutionary Otimization on Constrained Problems,” in Proc. The Fourth Annual Conf. on Evolutionary Programming, May. 1995.',

'J.-H. Kim and H.-S Shim, “Evolutionary Programming-Based Optimal Robust Locomotion Control of Autonomous Mobile Robots,” in Proc. The Fourth Annual Conf. on Evolutionary Programming, La Jolla, USA,, May. 1995.',

'J.-H. Kim and H.-S. Shim, “Robust Autonomous Location Control Using Evolutionary Programming for Autonomous Mobile Robots,” in Proc. The Fourth Annual Conf. on Evolutionary Programming, La Jolla, USA, May. 1995.',

'H. Myeong and J.-H. Kim, “Neural Network Learning using Time-Varying Two-Phase Optimization,” in Proc. the 33rd Conf. on Decision and Control, Dec. 1994.',

'J.-H. Kim and J.-M. Yang, “A Novel Organization Level Structure of the Intelligent Machine,” in Proc. Japan-Korea Joint Conf. on Robotics, Nov. 1994.',

'S.-W. Lee and J.-H. Kim, “Robust Adaptive Nonlinear Control Based on a Fuzzy Model,” in Proc. KFMS Fall Conf. 94, Japan, Oct. 1994.',

'J.-M. Yang and J.-H. Kim, “A Multisensor Decision Fusion Strategy Using Fuzzy Measure Theory,” in Proc. KFMS Fall Conf. 94, Japan, Oct. 1994.',

'S.-M. Yoo, U.-H. Kim and Y. Hwang and J.-H. Kim, “Type Anywhere You Want: An Introduction to Invisible Mobile Keyboard,” Proc. 2021 International Joint Conference on Artificial Intelligence (IJCAI), Aug. 2021.',

'J. Kim, I. Yoon, G.-M. Park, and J.-H. Kim. “Non-probabilistic cosine similarity loss for few-shot image classification,” in The 31st British Machine Vision Conference (BMVC), Virtual, Sep. 2020.',

'S.-J. Lee, J.-M. Park and D.-H. Kim and J.-H. Kim, “Adaptive Task Planner for Performing Home Service Tasks in Cooperation with a Human,” Proc. 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Oct. 2018.',

'W.-H. Lee and J.-H. Kim, “Social Relationship Development between Human and Robot through Real-time Face Identification and Emotional Interaction,” in Proc. ACM/IEEE International Conference on Human Robot Interaction, Video Abstract, (Best Video Award), Mar. 2018.',

'S.-H. Cho, W.-H. Lee and J.-H. Kim, “Implementation of Human-Robot VQA Interaction System with Dynamic Memory Networks,” in Proc. 2017 IEEE International Conference on Systems, Man, and Cybernetics, (Best Student Paper Award), Banff Center, Banff, Canada, Oct. 2017.',

'D. Sigmund, G.-M. Park and J.-H. Kim, “Context Preference-based Deep Adaptive Resonance Theory: Integrating User Preferences into Episodic Memory Encoding and Retrieval,” IEEE International Joint Conference on Neural Networks, May. 2017.',


'S. Gulshad, D. Sigmund and J.-H. Kim, “Learning to Reproduce Stochastic Time Series Using Stochastic LSTM,” IEEE International Joint Conference on Neural Networks, May. 2017.',


'S. Gulshad and J.-H. Kim, “Deep Convolutional and Recurrent Writer,” IEEE International Joint Conference on Neural Networks, May. 2017.',


'J.-M. Park J.-H. Kim, “Online recurrent extreme learning machine and its application to time-series prediction,” IEEE International Joint Conference on Neural Networks, May. 2017.',


'B.-S. Ko, H.-J. Choi, C.-S. Hong, J.-H. Kim, O.-C. Kwon and C.-D. Yoo, “Neural network-based autonomous navigation for a homecare mobile robot,” IEEE International Conference on Big Data and Smart Computing (BigComp), pp. 403-406, Feb. 2017.',


'M.-J. Kim, S.-H. Baek, S.-H. Cho and J.-H. Kim, “Approach to Integrate Episodic Memory into Cogency-based Behavior Planner for Robots,” in Proc. 2016 IEEE International Conference on Systems, Man, and Cybernetics, Oct. 2016.',


'G.-M. Park, S.-H. Cho and J.-H. Kim, “Biologically-Inspired Episodic Memory Model Considering the Context Information,” in Proc. 2016 IEEE International Conference on Systems, Man, and Cybernetics, Oct. 2016.',

'K.-M. Koo and J.-H. Kim, “A CMAC Network Based Controller,” in Proc. KAAC 94(Int. Session), Oct. 1994.',

'K.-M. Koo and J.-H. Kim, “On the Neural Network Based Controller,” in Proc. ICONIP 94, Seoul, Oct. 1994.',

'J.-H. Kim and H.-S. Shim, “Robust Locomotion Control of Autonomous Mobile Robot,” in Proc. Japan -Korea Joint Conf. on Robotics, Sep. 1994.',

'J.-H. Kim and K.-M. Koo, “On the Design of Robust Controller using CMAC,” in Proc. Japan-Korea Joint Conf. on Robotics, Sep. 1994.',

'J.-H. Kim and K.-Ch. Kim, “Fuzzy Control with Multicriteria Using Fuzzy Measure and Integrals,” in Proc. ISRAM, Hawaii, USA, Aug. 1994.',

'J.-H. Kim, K.-Ch. Kim and J.-Y. Jeon, “Fuzzy Expert System Based on Fuzzy Integral,” in Proc. IIZUKA, Aug. 1994.',

'J.-Y.Jeon, J.-M. Yang, H.-K. Chae and J.-H. Kim, “Generalized Predictive Control Using Fuzzy Neural Network Model,” in Proc. the Asian Control Conf., Tokyo, Japan, Jul. 1994.',

'J.-Y. Jeon and J.-H. Kim, “An Exponential Data Weighting Adaptive Observer and It’s Application to Indirect Adaptive Control,” in Proc. Asian Control Conf., Tokyo, Japan, Jul. 1994.',

'J.-H. Kim, S.-W. Lee and A.L.Fradkov, “Stable Direct Adaptive Control of Nonminimum Phase Systems,” in Proc. the Asian Control Conf., Tokyo, Japan, Jul. 1994.',

'K.-M. Koo and J.-H. Kim, “Robust Controller for Robot Manipulators with Parametric Uncertainty,” in Proc. the Asian Control Conf., Tokyo, Japan, Jul. 1994.',

'H. Myeong and J.-H. Kim, “Time Varying Two-Phase Optimization for Neural Network Learning with Weight Constraints,” in Proc. the Asian Control Conf, Tokyo, Japan, Jul. 1994.',

'H.-S. Shim and J.-H. Kim, “A Stable Locomotion Control of Autonomous Mobile Robot,” in Proc. the Asian Control Conf, Tokyo, Japan, Jul. 1994.',

'J.-Y.Jeon, J.-M. Yang, H.-K. Chae and J.-H. Kim, “Generalized Predictive Control Using Fuzzy Neural Network Model,” in Proc. the Asian Control Conf, Tokyo, Japan, Jul. 1994.',

'S.-W. Lee, J.-H. Kim and Edwin K.P.Chong, “Some Experiments with a Fuzzy Precompensated PD Controller,” in Proc. American Control Conf., Jun. 1994.',

'J.-H. Kim, “Multicriteria Fuzzy Control based on Fuzzy Measures and Integrals,” in Proc. IFSICC, Louisville, KY, Mar. 1994.',

'J.-H. Kim, J.-H. Park, S.-W. Lee and Edwin K.P.Chong, “Control of Systems with Deadzones using PD Controllers with Fuzzy Precompensation,” in Proc. the International Symp. on Intelligent Contr., Chicago, USA, Aug. 1993.',

'J.-H. Kim, J.-H. Park and S.-W. Lee, “A Two-Layered Fuzzy Controller for Systems with Deadzones,” in Proc. Fifth IFSA World Congress, Seoul, Korea, Jul. 1993.',

'J.-H. Kim, K.-M. Koo and H.-S. Shim, “Robust Direct Adaptive Control of Robot Manipulators,” in Proc. ISRAM, Santa Fe, U.S.A., Nov. 1992.',

'J.-H. Kim, S.W.Lee and A.L.Fradkov, “Inite Differential Speed-Gradient Algorithms for Direct Adaptive Control of Nonminimum Phase Systems,” in Proc. ACASP, Grenoble, France, Jul. 1992.',

'J.-H. Kim, “Robust Direct Adaptive Control with Exponential Data Weighting,” in Proc. American Control Conf., Illinois, U.S.A., Jun. 1992.',

'J.-H. Kim, “Direct Adaptive Control Using Specially Structured Nonminimal Model,” in Proc. Int. Symposium on the Mathematical Theory of Networks and Systems, Kobe, Japan, Jun. 1991.',

'J.-H. Kim, “Robust Model Reference Direct Adaptive Pole Placement Control,” in Proc. KACC, Int. Session, Seoul, Korea, Oct. 1990.',

'J.-H. Kim, Y.-Ch and K.-K Choi, “Direct Model Reference Adaptive Pole Placement Control with Exponential Weighting Properties,” in Proc. the 28th SICE Annual Conf., Japan, Jul. 1989.',

'J.-H. Kim, Y.-Ch and K.-K Choi, “Design of a Direct Model Reference Adaptive Pole Placement Control with Exponential Weighting Properties,” in Proc. A.C.C., USA, Jun. 1989.']


# year = []
# for i in range(len(paper)):
#     yr = paper[i].split(".")[-2]
#     year.append(yr)
# print(year)
#
# year_sort,  = np.sort(year)
# print(year_sort)
print(len(paper))
paper = sorted(paper, key=lambda x: x.split(".")[-2], reverse=True)
print(len(paper))
id = 0
for i in range(len(paper)):
    # yr = paper[i].split(".")[-2]
    print(paper[i], "\n")
    id+=1
    # print("\n")
print(id)
