<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b132b,50:1c2541,100:0b132b&height=220&section=header&text=COLLEGE%20MANAGEMENT%20SYSTEM&fontSize=34&fontColor=F1F5F9&animation=fadeIn&fontAlignY=38&desc=Flask%20%C2%B7%20SQLAlchemy%20%C2%B7%20MySQL%20%C2%B7%20Role-Based%20Access&descAlignY=58&descSize=16&descColor=5BC0BE" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Space+Grotesk&size=20&duration=3000&pause=1000&color=5BC0BE&center=true&vCenter=true&width=650&lines=Staff+marks+attendance...;HOD+allocates+subjects...;Admin+backs+up+the+database." alt="Typing SVG"/>

<br/><br/>

<p>
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Framework-Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/ORM-SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy"/>
  <img src="https://img.shields.io/badge/Database-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"/>
  <img src="https://img.shields.io/badge/License-Educational%20Use-7F5AF0?style=for-the-badge" alt="License"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Auth-Flask--Login-5BC0BE?style=flat-square" alt="Flask-Login"/>
  <img src="https://img.shields.io/badge/Roles-Admin%20%7C%20HOD%20%7C%20Staff-5BC0BE?style=flat-square" alt="Roles"/>
  <img src="https://img.shields.io/badge/Reports-PDF%20%2F%20Excel-5BC0BE?style=flat-square" alt="Reports"/>
</p>

<h3>🎓 A role-based college management system for attendance, internal assessments (CIE), staff allocation, and reporting</h3>

</div>

---

## 📖 Overview

The **College Management System (CMS)** is a Flask web application that automates day-to-day academic administration: attendance tracking, **CIE (Continuous Internal Evaluation)** marks, staff-to-subject allocation, student records, and database backup/restore — all behind role-based authentication for **Admin**, **HOD**, and **Staff** users.

<table align="center">
<tr>
<td align="center">🏗️<br/><b>Architecture</b><br/>Flask Blueprints (Route → Service → SQLAlchemy Model)</td>
<td align="center">🔐<br/><b>Auth</b><br/>Flask-Login, role-gated routes</td>
<td align="center">🗄️<br/><b>Data Layer</b><br/>SQLAlchemy + Flask-Migrate</td>
<td align="center">📄<br/><b>Reports</b><br/>PDF (reportlab/fpdf2) & Excel (pandas/openpyxl)</td>
</tr>
</table>

## ✨ Features

<table align="center" width="100%">
<tr>
<td width="25%" valign="top">

### 👤 Access Control
- Role-based login (Admin / HOD / Staff)
- Secure session auth (Flask-Login)
- User & role management

</td>
<td width="25%" valign="top">

### 📝 Attendance & CIE
- Attendance marking & tracking
- CIE paper & marks management
- CIE configuration per subject

</td>
<td width="25%" valign="top">

### 📚 Academics
- Student, batch, branch & class records
- Subject management
- Staff allocation to subjects/classes

</td>
<td width="25%" valign="top">

### 📊 Reports & Data
- PDF & Excel report generation
- Database backup & restore (.xlsx)
- Bulk student upload templates

</td>
</tr>
</table>

## 🛠️ Technology Stack

<div align="center">

![My Skills](https://skillicons.dev/icons?i=python,flask,mysql,html,css,js,git)

</div>

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login |
| **Database** | MySQL (via PyMySQL) |
| **Reports** | reportlab, fpdf2, pandas, openpyxl |
| **Security** | cryptography, python-dotenv |
| **Frontend** | HTML5, CSS3, JavaScript (Jinja2 templates) |

## 🏗️ Architecture & Workflow

```mermaid
flowchart TD
    A["🌐 Browser<br/>Admin / HOD / Staff"] -->|"HTTP Request"| B["🛣️ Flask Route<br/>admin_routes / hod_routes / staff_routes / auth_routes"]
    B --> C["🔐 Flask-Login<br/>role check"]
    C --> D["⚙️ Service Layer<br/>attendance / cie / allocation / report / backup"]
    D --> E["🗄️ SQLAlchemy Models"]
    E --> F[("🐬 MySQL")]
    F --> E
    E --> D
    D -->|"Render"| G["🎨 Jinja2 Template"]
    G -->|"Rendered HTML"| A

    B -.->|"JSON"| H["🔌 API Blueprint<br/>student / attendance / cie / allocation / report / backup"]
    H --> D

    style A fill:#0b132b,stroke:#5BC0BE,color:#ffffff
    style C fill:#1c2541,stroke:#ff4d6d,color:#ffffff
    style G fill:#0b132b,stroke:#3A506B,color:#ffffff
    style F fill:#1c2541,stroke:#7f5af0,color:#ffffff
    style H fill:#1c2541,stroke:#5BC0BE,color:#ffffff
```

**Request flow:** page routes (`admin_routes`, `hod_routes`, `staff_routes`, `auth_routes`) render server-side templates, while a parallel set of API blueprints (`student_api`, `attendance_api`, `cie_api`, `allocation_api`, `report_api`, `backup_api`) handle data operations. Both paths go through the same service layer down to SQLAlchemy models backed by MySQL.

## 📂 Domain Model

Core models: `User`, `Role`, `Student`, `Batch`, `Branch`, `ClassModel`, `Subjects`, `StaffAllocation`, `Attendance`, `CieConfig`, `CieMarks`, `CiePapers`, `BackupLog`, `Setting`, `Control`, `Maintain`.

## 📸 Screenshots & Demo

> 🖼️ Add your actual screenshots to `docs/screenshots/` and update the filenames below.

<div align="center">
<table>
<tr>
<td align="center" width="50%">
<img src="./docs/screenshots/admin-dashboard.png" alt="Admin dashboard — PLACEHOLDER" width="100%"/>
<br/><b>Admin Dashboard</b>
</td>
<td align="center" width="50%">
<img src="./docs/screenshots/attendance.png" alt="Attendance — PLACEHOLDER" width="100%"/>
<br/><b>Attendance Management</b>
</td>
</tr>
<tr>
<td align="center" width="50%">
<img src="./docs/screenshots/cie-marks.png" alt="CIE marks — PLACEHOLDER" width="100%"/>
<br/><b>CIE Marks Entry</b>
</td>
<td align="center" width="50%">
<img src="./docs/screenshots/reports.png" alt="Reports — PLACEHOLDER" width="100%"/>
<br/><b>Report Generation</b>
</td>
</tr>
</table>
</div>

## 🚀 Installation

**1. Clone the repository**
```bash
git clone https://github.com/Nesara29/CMS.git
cd CMS
```

**2. Create a virtual environment & install dependencies**
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

**3. Configure the database**

Set your MySQL connection string and secret keys in `config/config.py` or a `.env` file (loaded via `python-dotenv`).

**4. Run database migrations**
```bash
flask db upgrade
```

**5. Run the application**
```bash
python app.py
```

**6. Open your browser**
```
http://127.0.0.1:5000
```

## 📂 Project Structure

```
CMS/
├── app.py
├── wsgi.py
├── extensions.py
├── config/
│   └── config.py
├── models/                 → student, staff_allocation, attendance, cie_marks,
│                              cie_papers, cie_config, batch, branch, subjects,
│                              class_model, role, user, backup_log, setting, control
├── routes/                 → admin_routes, hod_routes, staff_routes, auth_routes
├── api/                    → student_api, attendance_api, cie_api,
│                              allocation_api, report_api, backup_api
├── services/                → attendance_service, cie_service, allocation_service,
│                              report_service, backup_service, auth_service
├── utils/                  → decorators, file_handler, pdf_generator,
│                              password_utils, seed_data
├── templates/               → admin.html, hod.html, staff.html, login.html,
│                              manage_users.html, report_pdf.html
├── migrations/              → Alembic migration scripts
├── backups/                 → generated .xlsx database backups
├── uploads/cie_papers/       → uploaded CIE paper files
├── logs/app.log
├── requirements.txt
└── README.md
```

## 🎯 Learning Outcomes

🐍 Python & Flask &nbsp;•&nbsp; 🗄️ SQLAlchemy ORM & Alembic migrations &nbsp;•&nbsp; 🔐 Flask-Login role-based access &nbsp;•&nbsp; 📄 PDF generation (reportlab/fpdf2) &nbsp;•&nbsp; 📊 Excel import/export (pandas/openpyxl) &nbsp;•&nbsp; 🐬 MySQL relational design &nbsp;•&nbsp; 🔌 Blueprint-based API design &nbsp;•&nbsp; 🔒 Data encryption with `cryptography`

## 📈 Future Enhancements

<table align="center">
<tr>
<td>🌐 Online Student Portal</td>
<td>👪 Parent Portal</td>
<td>💳 Fee Management System</td>
</tr>
<tr>
<td>🗓️ Timetable Management</td>
<td>📝 Examination Management</td>
<td>📧 Email & SMS Notifications</td>
</tr>
<tr>
<td>🔑 Finer-Grained Role Permissions</td>
<td>📱 Mobile Application Support</td>
<td>☁️ Cloud Deployment</td>
</tr>
</table>

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Submit a Pull Request.

## 👨‍💻 Developer

<div align="center">

| | |
|---|---|
| 🧑‍💻 **Name** | `NESARA` |
| 🐙 **GitHub** | https://github.com/Nesara29 |

</div>

## 🔗 Project Links

<div align="center">

<a href="https://github.com/Nesara29/CMS">
  <img src="https://img.shields.io/badge/Repository-CMS-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repository"/>
</a>
<a href="https://github.com/Nesara29/CMS/issues">
  <img src="https://img.shields.io/badge/Report-Issue-red?style=for-the-badge&logo=github&logoColor=white" alt="Issues"/>
</a>
<a href="https://github.com/Nesara29/CMS/fork">
  <img src="https://img.shields.io/badge/Fork-Project-2CB67D?style=for-the-badge&logo=github&logoColor=white" alt="Fork"/>
</a>

</div>

## 📄 License

This project is licensed for **educational and learning purposes**. You are free to use and modify it for academic or personal projects.

## ⭐ Support

If you found this project useful, please give it a **⭐ Star** on GitHub.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1c2541,50:0b132b,100:1c2541&height=120&section=footer"/>

</div>

