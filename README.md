# Face Recognition Attendance System

## Overview

This project is a desktop application developed using Python, Tkinter, Convolutional Neural Networks (CNN), and MySQL. It automates the process of recording attendance by recognizing faces, offering a more efficient and secure alternative to traditional methods.

## Features

- **User Registration:** Capture and store facial images of new users.
- **Face Recognition:** Identify and verify users in real-time using CNN.
- **Attendance Logging:** Automatically record attendance upon successful recognition.
- **Database Management:** Store user information and attendance records in a MySQL database.
- **User Interface:** Intuitive GUI developed with Tkinter for seamless interaction.

## Technologies Used

- **Programming Language:** Python
- **Libraries:** Tkinter, OpenCV, NumPy
- **Machine Learning:** Convolutional Neural Networks (CNN)
- **Database:** MySQL

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RAKIBUL424/face_recognition_attendence_system.git
   cd face_recognition_attendence_system
   ```

2. **Install Dependencies:**
   Ensure you have Python installed. Then, install the required libraries:
   ```bash
   pip install tkinter opencv-python numpy mysql-connector-python
   ```

3. **Set Up the Database:**
   - Install MySQL and create a database named `attendance_system`.
   - Execute the SQL commands in `database_setup.sql` to create necessary tables.

4. **Run the Application:**
   ```bash
   python main.py
   ```

## Usage

- **Register a New User:** Navigate to the 'Register' section, enter user details, and capture facial images.
- **Mark Attendance:** The system will automatically recognize registered users and log their attendance.
- **View Records:** Access attendance logs through the 'View Records' section.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is open-source 
