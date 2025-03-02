import streamlit as st
import sqlite3

# -----------------------------
# Course Library (Local Dataset)
# -----------------------------
course_library = [
    {"title": "Introduction to Python",
     "description": "Learn Python basics and start programming.",
     "topics": ["python", "programming"]},
    {"title": "Advanced Python Techniques",
     "description": "Deep dive into advanced Python topics and libraries.",
     "topics": ["python", "advanced", "programming"]},
    {"title": "Data Science with Python",
     "description": "Apply Python for data analysis and visualization.",
     "topics": ["python", "data science", "analytics"]},
    {"title": "Python for Data Analysis",
     "description": "Learn how to analyze data using Python libraries.",
     "topics": ["python", "data analysis", "pandas"]},
    {"title": "Machine Learning 101",
     "description": "Introduction to machine learning concepts and algorithms.",
     "topics": ["machine learning", "ai"]},
    {"title": "Deep Learning Fundamentals",
     "description": "Learn the basics of deep learning and neural networks.",
     "topics": ["deep learning", "ai", "machine learning"]},
    {"title": "Introduction to Java",
     "description": "Learn the fundamentals of Java programming.",
     "topics": ["java", "programming"]},
    {"title": "Advanced Java Programming",
     "description": "Master advanced Java programming techniques.",
     "topics": ["java", "advanced", "programming"]},
    {"title": "Java for Web Development",
     "description": "Learn how to build web applications using Java.",
     "topics": ["java", "web development", "programming"]},
    {"title": "Java Design Patterns",
     "description": "Understand common design patterns used in Java development.",
     "topics": ["java", "design patterns", "programming"]},
    {"title": "JavaScript Essentials",
     "description": "Learn the basics of JavaScript for web development.",
     "topics": ["javascript", "programming", "web development"]},
    {"title": "Modern JavaScript Programming",
     "description": "Explore ES6+ features and modern JavaScript practices.",
     "topics": ["javascript", "advanced", "web development"]},
    {"title": "React for Beginners",
     "description": "Learn how to build user interfaces with React.",
     "topics": ["react", "javascript", "web development"]},
    {"title": "Advanced React Development",
     "description": "Deep dive into state management and advanced React patterns.",
     "topics": ["react", "advanced", "javascript"]},
    {"title": "Vue.js Fundamentals",
     "description": "Get started with building applications using Vue.js.",
     "topics": ["vue.js", "javascript", "web development"]},
    {"title": "Angular for Developers",
     "description": "Learn how to build dynamic web apps using Angular.",
     "topics": ["angular", "typescript", "web development"]},
    {"title": "HTML & CSS Basics",
     "description": "Learn the building blocks of web development: HTML and CSS.",
     "topics": ["html", "css", "web development"]},
    {"title": "Responsive Web Design",
     "description": "Design websites that work on any device.",
     "topics": ["responsive design", "css", "web development"]},
    {"title": "Full Stack Web Development",
     "description": "Learn both front-end and back-end development techniques.",
     "topics": ["full stack", "web development", "programming"]},
    {"title": "Backend Development with Node.js",
     "description": "Build scalable back-end applications using Node.js.",
     "topics": ["node.js", "backend", "javascript"]},
    {"title": "Database Design & SQL",
     "description": "Learn how to design databases and write SQL queries.",
     "topics": ["database", "sql", "data management"]},
    {"title": "NoSQL Databases",
     "description": "Explore non-relational databases like MongoDB and Cassandra.",
     "topics": ["nosql", "mongodb", "database"]},
    {"title": "Data Visualization with D3.js",
     "description": "Create interactive visualizations with D3.js.",
     "topics": ["data visualization", "d3.js", "javascript"]},
    {"title": "Data Visualization with Python",
     "description": "Visualize data using Python libraries like Matplotlib and Seaborn.",
     "topics": ["data visualization", "python", "data science"]},
    {"title": "Data Analysis with Pandas",
     "description": "Master data manipulation and analysis using Pandas.",
     "topics": ["pandas", "python", "data analysis"]},
    {"title": "Statistics for Data Science",
     "description": "Learn fundamental statistics concepts for data science applications.",
     "topics": ["statistics", "data science", "analytics"]},
    {"title": "Introduction to R",
     "description": "Get started with R programming for data analysis.",
     "topics": ["r", "data science", "programming"]},
    {"title": "Advanced R Programming",
     "description": "Explore advanced concepts in R for data analysis.",
     "topics": ["r", "advanced", "data science"]},
    {"title": "Data Science with R",
     "description": "Apply R programming to solve data science problems.",
     "topics": ["r", "data science", "analytics"]},
    {"title": "Introduction to Machine Learning",
     "description": "Learn the basics of machine learning algorithms and applications.",
     "topics": ["machine learning", "ai", "data science"]},
    {"title": "Supervised Learning Techniques",
     "description": "Understand supervised learning methods and algorithms.",
     "topics": ["machine learning", "supervised learning", "ai"]},
    {"title": "Unsupervised Learning Methods",
     "description": "Discover unsupervised learning techniques and clustering algorithms.",
     "topics": ["machine learning", "unsupervised learning", "ai"]},
    {"title": "Neural Networks and Deep Learning",
     "description": "Learn how to build and train neural networks.",
     "topics": ["deep learning", "neural networks", "ai"]},
    {"title": "Computer Vision Basics",
     "description": "Introduction to computer vision and image processing.",
     "topics": ["computer vision", "ai", "machine learning"]},
    {"title": "Natural Language Processing Fundamentals",
     "description": "Learn how to process and analyze natural language data.",
     "topics": ["nlp", "ai", "machine learning"]},
    {"title": "Reinforcement Learning Essentials",
     "description": "Understand the basics of reinforcement learning and decision-making.",
     "topics": ["reinforcement learning", "ai", "machine learning"]},
    {"title": "Artificial Intelligence Overview",
     "description": "Explore various concepts and applications in artificial intelligence.",
     "topics": ["ai", "machine learning", "technology"]},
    {"title": "Introduction to Cybersecurity",
     "description": "Learn the basics of cybersecurity and threat protection.",
     "topics": ["cybersecurity", "security", "technology"]},
    {"title": "Ethical Hacking Fundamentals",
     "description": "Get introduced to ethical hacking techniques and tools.",
     "topics": ["ethical hacking", "cybersecurity", "security"]},
    {"title": "Cloud Computing Essentials",
     "description": "Learn the fundamentals of cloud computing and its services.",
     "topics": ["cloud computing", "aws", "azure", "gcp"]},
    {"title": "AWS Cloud Practitioner",
     "description": "Prepare for the AWS Cloud Practitioner certification with foundational cloud knowledge.",
     "topics": ["aws", "cloud computing", "certification"]},
    {"title": "Microsoft Azure Fundamentals",
     "description": "Learn the basics of Microsoft Azure cloud services.",
     "topics": ["azure", "cloud computing", "microsoft"]},
    {"title": "Google Cloud Platform Basics",
     "description": "Introduction to Google Cloud Platform and its services.",
     "topics": ["gcp", "cloud computing", "google"]},
    {"title": "DevOps Fundamentals",
     "description": "Learn the principles and tools of DevOps for efficient development.",
     "topics": ["devops", "automation", "software engineering"]},
    {"title": "Docker & Containerization",
     "description": "Understand containerization with Docker for streamlined deployments.",
     "topics": ["docker", "containers", "devops"]},
    {"title": "Kubernetes for Beginners",
     "description": "Learn how to orchestrate containers using Kubernetes.",
     "topics": ["kubernetes", "containers", "devops"]},
    {"title": "Microservices Architecture",
     "description": "Understand the design and implementation of microservices.",
     "topics": ["microservices", "architecture", "backend"]},
    {"title": "Agile Software Development",
     "description": "Explore agile methodologies and frameworks for software development.",
     "topics": ["agile", "scrum", "software development"]},
    {"title": "Software Testing & QA",
     "description": "Learn essential techniques for software testing and quality assurance.",
     "topics": ["testing", "qa", "software development"]},
    {"title": "Mobile App Development with React Native",
     "description": "Build cross-platform mobile apps using React Native.",
     "topics": ["react native", "mobile development", "javascript"]},
    {"title": "iOS App Development with Swift",
     "description": "Learn to develop iOS applications using Swift.",
     "topics": ["ios", "swift", "mobile development"]},
    {"title": "Android App Development with Kotlin",
     "description": "Build Android apps using Kotlin programming language.",
     "topics": ["android", "kotlin", "mobile development"]},
    {"title": "Cross-Platform App Development with Flutter",
     "description": "Develop high-performance apps using Flutter and Dart.",
     "topics": ["flutter", "dart", "mobile development"]},
    {"title": "Game Development with Unity",
     "description": "Learn game development using the Unity engine.",
     "topics": ["unity", "game development", "c#"]},
    {"title": "Virtual Reality Development",
     "description": "Explore the fundamentals of virtual reality app development.",
     "topics": ["vr", "virtual reality", "game development"]},
    {"title": "Augmented Reality Essentials",
     "description": "Learn how to create augmented reality experiences.",
     "topics": ["ar", "augmented reality", "technology"]},
    {"title": "Blockchain Basics",
     "description": "Understand the core concepts behind blockchain technology.",
     "topics": ["blockchain", "cryptocurrency", "technology"]},
    {"title": "Ethereum and Smart Contracts",
     "description": "Learn to develop smart contracts on the Ethereum platform.",
     "topics": ["ethereum", "blockchain", "smart contracts"]},
    {"title": "Cryptocurrency Fundamentals",
     "description": "Explore the basics of cryptocurrencies and digital assets.",
     "topics": ["cryptocurrency", "blockchain", "finance"]},
    {"title": "Internet of Things (IoT) Basics",
     "description": "Introduction to IoT concepts and applications.",
     "topics": ["iot", "technology", "automation"]},
    {"title": "Robotics for Beginners",
     "description": "Learn the fundamentals of robotics and automation.",
     "topics": ["robotics", "automation", "engineering"]},
    {"title": "Data Engineering Fundamentals",
     "description": "Understand the principles of data engineering and pipeline design.",
     "topics": ["data engineering", "big data", "analytics"]},
    {"title": "Big Data with Hadoop",
     "description": "Learn to process and analyze big data using Hadoop.",
     "topics": ["big data", "hadoop", "data engineering"]},
    {"title": "Spark for Data Processing",
     "description": "Use Apache Spark for fast, large-scale data processing.",
     "topics": ["spark", "big data", "data processing"]},
    {"title": "SQL for Data Analysis",
     "description": "Enhance your data analysis skills with SQL queries.",
     "topics": ["sql", "data analysis", "database"]},
    {"title": "NoSQL with MongoDB",
     "description": "Learn how to use MongoDB for flexible data storage.",
     "topics": ["mongodb", "nosql", "database"]},
    {"title": "Python Scripting for Automation",
     "description": "Automate tasks using Python scripting.",
     "topics": ["python", "automation", "scripting"]},
    {"title": "Introduction to Scripting with Bash",
     "description": "Learn the basics of Bash scripting on Linux.",
     "topics": ["bash", "scripting", "linux"]},
    {"title": "PowerShell for Administrators",
     "description": "Automate Windows tasks with PowerShell scripting.",
     "topics": ["powershell", "scripting", "windows"]},
    {"title": "System Administration Basics",
     "description": "Learn essential skills for system administration.",
     "topics": ["system administration", "linux", "windows"]},
    {"title": "Linux Essentials",
     "description": "Get started with Linux system usage and commands.",
     "topics": ["linux", "system administration", "opensource"]},
    {"title": "Networking Fundamentals",
     "description": "Understand the basics of computer networking.",
     "topics": ["networking", "IT", "cybersecurity"]},
    {"title": "Introduction to Ethical AI",
     "description": "Explore the ethical considerations of AI technologies.",
     "topics": ["ai", "ethics", "technology"]},
    {"title": "AI and Society",
     "description": "Examine the societal impacts of artificial intelligence.",
     "topics": ["ai", "society", "ethics"]},
    {"title": "Quantum Computing Basics",
     "description": "Learn the foundational concepts of quantum computing.",
     "topics": ["quantum computing", "technology", "computing"]},
    {"title": "Statistical Modeling with Python",
     "description": "Apply statistical models using Python libraries.",
     "topics": ["python", "statistics", "data science"]},
    {"title": "Time Series Analysis",
     "description": "Learn techniques for analyzing time-series data.",
     "topics": ["time series", "data analysis", "python"]},
    {"title": "Forecasting with Python",
     "description": "Develop forecasting models using Python.",
     "topics": ["forecasting", "python", "data science"]},
    {"title": "Financial Data Analysis",
     "description": "Analyze financial data using analytical tools.",
     "topics": ["finance", "data analysis", "python"]},
    {"title": "FinTech Fundamentals",
     "description": "Learn the basics of financial technology and innovations.",
     "topics": ["fintech", "finance", "technology"]},
    {"title": "E-commerce Web Development",
     "description": "Build and manage e-commerce websites.",
     "topics": ["e-commerce", "web development", "business"]},
    {"title": "Digital Marketing Essentials",
     "description": "Learn the strategies and tools of digital marketing.",
     "topics": ["digital marketing", "marketing", "business"]},
    {"title": "SEO Basics",
     "description": "Understand search engine optimization techniques.",
     "topics": ["seo", "digital marketing", "business"]},
    {"title": "Social Media Marketing Strategies",
     "description": "Develop effective social media marketing campaigns.",
     "topics": ["social media", "marketing", "business"]},
    {"title": "Content Marketing Essentials",
     "description": "Learn how to create compelling content for marketing.",
     "topics": ["content marketing", "marketing", "business"]},
    {"title": "Graphic Design for Beginners",
     "description": "Get started with graphic design principles and tools.",
     "topics": ["graphic design", "design", "creativity"]},
    {"title": "Adobe Photoshop Fundamentals",
     "description": "Learn the basics of Adobe Photoshop for digital design.",
     "topics": ["photoshop", "graphic design", "design"]},
    {"title": "Adobe Illustrator Basics",
     "description": "Master the essentials of Adobe Illustrator.",
     "topics": ["illustrator", "graphic design", "design"]},
    {"title": "UI/UX Design Principles",
     "description": "Learn best practices for user interface and user experience design.",
     "topics": ["ui/ux", "design", "web development"]},
    {"title": "Product Design Fundamentals",
     "description": "Understand the process of designing a product from scratch.",
     "topics": ["product design", "design", "business"]},
    {"title": "Project Management Basics",
     "description": "Learn the fundamentals of effective project management.",
     "topics": ["project management", "business", "leadership"]},
    {"title": "Scrum & Agile Project Management",
     "description": "Master agile methodologies and Scrum practices.",
     "topics": ["scrum", "agile", "project management"]},
    {"title": "Business Analytics with Excel",
     "description": "Use Excel to perform data analysis and business forecasting.",
     "topics": ["excel", "business analytics", "data analysis"]},
    {"title": "Data-Driven Decision Making",
     "description": "Learn how to leverage data for strategic decision-making.",
     "topics": ["data analytics", "business", "decision making"]},
    {"title": "Introduction to Entrepreneurship",
     "description": "Explore the fundamentals of starting your own business.",
     "topics": ["entrepreneurship", "business", "startup"]},
    {"title": "Startup Fundamentals",
     "description": "Learn key strategies for launching and growing a startup.",
     "topics": ["startup", "entrepreneurship", "business"]},
    {"title": "Leadership and Management Skills",
     "description": "Develop effective leadership and management techniques.",
     "topics": ["leadership", "management", "business"]},
    {"title": "Communication Skills for Professionals",
     "description": "Improve your communication skills for the workplace.",
     "topics": ["communication", "soft skills", "professional development"]},
    {"title": "Critical Thinking and Problem Solving",
     "description": "Enhance your critical thinking and problem-solving abilities.",
     "topics": ["critical thinking", "problem solving", "skills"]},
    {"title": "Personal Development and Productivity",
     "description": "Learn techniques to boost productivity and personal growth.",
     "topics": ["personal development", "productivity", "self-improvement"]}
]

def get_recommendations(goal, library):
    """Simple keyword-based matching to simulate AI recommendations."""
    recommendations = []
    if goal:
        keywords = goal.lower().split()
        for course in library:
            score = sum(1 for keyword in keywords 
                        if any(keyword in topic.lower() for topic in course["topics"]))
            if score > 0:
                recommendations.append((score, course))
        recommendations.sort(key=lambda x: x[0], reverse=True)
        return [course for score, course in recommendations]
    return []

# -----------------------------
# Database Setup (SQLite)
# -----------------------------
conn = sqlite3.connect('user_data.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        goal TEXT,
        progress TEXT
    )
''')
conn.commit()

# -----------------------------
# Streamlit User Interface
# -----------------------------
st.set_page_config(page_title="AI Learning Assistant", layout="wide")

# Language selection
language = st.sidebar.selectbox("Select Language", ["English", "العربية"])

# Define labels based on language
if language == "English":
    title = "AI-Powered Learning Assistant"
    name_label = "Enter your name:"
    goal_label = "What do you want to learn?"
    recommendation_button = "Get Recommendations"
    recommendation_header = "Recommended Courses"
    no_rec_text = "No recommendations found. Please try a different goal."
    progress_title = "User Learning Progress"
else:
    title = "مساعد التعلم المعتمد على الذكاء الاصطناعي"
    name_label = "أدخل اسمك:"
    goal_label = "ماذا تريد أن تتعلم؟"
    recommendation_button = "احصل على التوصيات"
    recommendation_header = "الدورات الموصى بها"
    no_rec_text = "لم يتم العثور على توصيات. يرجى تجربة هدف مختلف."
    progress_title = "تقدم المستخدم في التعلم"

st.title(title)

# User input fields
name = st.text_input(name_label,"Faraz")
learning_goal = st.text_area(goal_label,"Python")

if st.button(recommendation_button):
    # Get recommendations based on user's learning goal
    recommendations = get_recommendations(learning_goal, course_library)
    
    if recommendations:
        st.subheader(recommendation_header)
        for course in recommendations:
            st.markdown(f"**{course['title']}**")
            st.write(course['description'])
    else:
        st.write(no_rec_text)
    
    # Save user input and progress to the database
    cursor.execute("INSERT INTO users (name, goal, progress) VALUES (?, ?, ?)",
                   (name, learning_goal, "Started"))
    conn.commit()

# Display user progress
st.subheader(progress_title)
cursor.execute("SELECT name, goal, progress FROM users")
users = cursor.fetchall()
for user in users:
    st.write(f"{user[0]} - {user[1]} - {user[2]}")

conn.close()
