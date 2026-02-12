# Projects Portfolio

## Current Projects

### AI Portfolio Assistant (2025 - Present)
**Live Demo**: https://portfolio-anthony-lesenfans.vercel.app/  
**Backend API**: https://ai-assistant-portfolio-eka7.onrender.com  
**Technologies**: FastAPI, LangChain, FAISS, Google Gemini, Next.js 14, TypeScript, Tailwind CSS

#### Description
Full-stack RAG (Retrieval Augmented Generation) chatbot integrated into professional portfolio, allowing recruiters and visitors to ask questions about my professional profile, experience, and skills in natural language.

#### Architecture
- **Backend**: FastAPI microservice with stateless session management
- **RAG System**: LangChain + FAISS vector database for semantic search
- **LLM**: Google Gemini Flash (free tier) for natural language generation
- **Frontend**: Next.js 14 with App Router, React, TypeScript
- **Styling**: Tailwind CSS with Framer Motion animations
- **Deployment**: Backend on Render, Frontend on Vercel
- **CI/CD**: GitHub Actions for automated testing and deployment

#### Features
- **Intelligent Chatbot**: Answers questions about experience, skills, projects using RAG
- **Bilingual Support**: French and English interface with automatic language detection
- **Responsive Design**: Mobile-first design with smooth animations
- **SEO Optimized**: Dynamic sitemap, metadata, Open Graph, Twitter Cards
- **Session Management**: Client-side conversation history (last 20 messages sent to backend)
- **Wake-up Notification**: Alerts users when backend is waking from sleep (Render free tier)
- **Source Attribution**: Displays source documents for each response
- **Markdown Rendering**: Rich text formatting in chat responses

#### Technical Highlights
- **Stateless Backend**: No server-side session storage, history sent from client
- **Vector Search**: FAISS for efficient semantic similarity search
- **Embeddings**: Google Gemini Embeddings for document vectorization
- **Chunking Strategy**: Recursive text splitting with 1000 char chunks, 200 char overlap
- **Context Window**: Last 20 messages for conversation continuity
- **Error Handling**: Graceful degradation with user-friendly error messages
- **Performance**: Optimized for Gemini free tier (20 requests/day limit)

#### DevOps & Quality
- **Docker**: Multi-stage builds for backend containerization
- **CI/CD Pipeline**: Automated testing, linting, security scanning
- **Testing**: Pytest for backend API tests
- **Code Quality**: Black formatting, Flake8 linting, Bandit security scanning
- **Monitoring**: Vercel Analytics and Speed Insights for frontend performance

#### Skills Demonstrated
- Full-stack development (FastAPI + Next.js)
- RAG system design and implementation
- LLM integration and prompt engineering
- Vector databases and semantic search
- Modern frontend development (React, TypeScript, Tailwind)
- Cloud deployment and DevOps
- API design and stateless architecture
- Real-time user experience optimization

---

### Dungeon Twister: Prison - Video Game Adaptation
**Duration**: May 2020 - April 2023  
**Technologies**: Python, OpenGL, FastAPI, Raspberry Pi, Pyinstaller

#### Description
Complete video game adaptation of the board game "Dungeon Twister: Prison" with 2D graphics engine, multiplayer support, and automatic update system.

#### Features
- **2D Graphics Engine**: Custom-built using OpenGL for smooth rendering
- **Game Modes**: 
  - Single player vs AI
  - Local Area Network (LAN) multiplayer
- **Embedded Server**: FastAPI server running on Raspberry Pi for game distribution
- **Auto-Update System**: Automatic game updates downloaded from Raspberry Pi server
- **Deployment**: Packaged with Pyinstaller for easy distribution

#### Technical Architecture
- **Graphics**: OpenGL for 2D rendering and animations
- **Networking**: Socket programming for LAN multiplayer
- **Backend**: FastAPI REST API for game distribution and updates
- **Hardware**: Raspberry Pi as dedicated game server
- **Packaging**: Pyinstaller for cross-platform executable

#### Skills Demonstrated
- Game development and graphics programming
- Network programming and multiplayer architecture
- API design for game distribution
- Embedded systems (Raspberry Pi)
- Software architecture and design patterns
- Cross-platform deployment

---

## Academic Projects (ESIEA Engineering School)

### Weakly Supervised Learning on Random Forests
**Type**: Research Project  
**Technologies**: Python, Scikit-learn, Machine Learning

- Implemented weakly supervised learning algorithms
- Optimized Random Forest models for limited labeled data
- Conducted experiments and performance analysis

### Robot Simulation with TDD
**Type**: Software Architecture Project  
**Technologies**: Python, GitHub Actions, pytest

- Developed robot simulation on spherical map in team environment
- Implemented Test-Driven Development (TDD) methodology
- Set up integration tests on GitHub with automated CI
- Practiced agile development and code review

### REST API Mobile Application
**Type**: Mobile Development Project  
**Technologies**: Android, Java, MVC Architecture, MDC Components

- Built mobile app displaying data from REST API
- Implemented MVC architecture pattern
- Used Material Design Components for UI

### Online Flashcard Website
**Type**: Web Development Project  
**Technologies**: JavaScript, Node.js, npm, Cookies

- Created web application for flashcard creation and study
- Implemented cookie-based data persistence
- Built responsive user interface

### AR Bee Behavior Simulation
**Type**: Augmented Reality Project  
**Technologies**: Unity, C#, ARCore, Android

- Developed AR application simulating bee behavior
- Implemented plane detection and image tracking
- Created realistic 3D animations and interactions

---

## Technical Projects at Thales

### License Plate Recognition System
**Technologies**: Python, Deep Learning, OpenCV, Jetson Nano

- Real-time license plate detection and recognition
- Deployed on NVIDIA Jetson Nano embedded board
- Achieved 95%+ accuracy in various lighting conditions

### Parking Space Detection System
**Technologies**: Python, Computer Vision, SQLite

- Automated detection of free parking spaces from video
- Database storage for historical data and analytics
- Real-time processing with low latency

### Train Station Fraud Detection
**Technologies**: Python, Deep Learning, Embedded Systems

- Embedded module for detecting fraudulent behavior at gates
- Real-time video analysis on edge device
- Integration with existing security infrastructure

---

## Skills Demonstrated Across Projects

### AI & Machine Learning
- RAG system implementation
- LLM integration and prompt engineering
- Deep Learning for computer vision
- Weakly supervised learning
- Model optimization for production

### Full-Stack Development
- **Frontend**: React, Next.js, TypeScript, Tailwind CSS
- **Backend**: FastAPI, Node.js, REST APIs
- **Databases**: FAISS, SQLite, MongoDB
- **Real-time**: WebSockets, LAN networking

### Graphics & Game Development
- OpenGL 2D graphics programming
- Game architecture and design patterns
- Multiplayer networking
- Physics and collision detection

### DevOps & Deployment
- Docker containerization
- CI/CD with GitHub Actions
- Cloud deployment (Vercel, Render)
- Embedded systems (Raspberry Pi, Jetson Nano)

### Software Engineering
- Test-Driven Development (TDD)
- Agile methodologies
- Code review and collaboration
- Technical documentation
- Version control (Git)

### Domain Expertise
- Computer Vision and Image Processing
- Natural Language Processing
- Telecommunications (5G/4G)
- Game Development
- Embedded Systems
