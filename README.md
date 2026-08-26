<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:1a1440,100:0f0c29&height=220&section=header&text=ACADEMIC%20DATA%20MANAGEMENT&fontSize=38&fontColor=EDEAE0&animation=fadeIn&fontAlignY=38&desc=Python%20%C2%B7%20Flask%20%C2%B7%20SQLAlchemy%20%C2%B7%20MySQL&descAlignY=58&descSize=17&descColor=00d4ff" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Space+Grotesk&size=20&duration=3000&pause=1000&color=7F5AF0&center=true&vCenter=true&width=650&lines=Manage+students%2C+branches+%26+classes...;Track+attendance+and+CIE+marks...;Generate+PDF%2FExcel+reports+and+backups." alt="Typing SVG"/>

<br/><br/>

<p>
  <img src="https://img.shields.io/badge/Language-Python%203.11-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Language: Python 3.11"/>
  <img src="https://img.shields.io/badge/Framework-Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Framework: Flask"/>
  <img src="https://img.shields.io/badge/ORM-SQLAlchemy-D71000?style=for-the-badge" alt="ORM: Flask-SQLAlchemy"/>
  <img src="https://img.shields.io/badge/Database-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="Database: MySQL"/>
  <img src="https://img.shields.io/badge/License-Educational%20Use-7F5AF0?style=for-the-badge" alt="License: Educational Use"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Security-Flask--Login%20%2B%20Cryptography-red?style=flat-square" alt="Flask Login"/>
  <img src="https://img.shields.io/badge/Roles-Admin%20%7C%20HOD%20%7C%20Staff-blueviolet?style=flat-square" alt="Roles"/>
  <img src="https://img.shields.io/badge/Reporting-ReportLab%20%2B%20Pandas-blue?style=flat-square" alt="Reporting"/>
</p>

<h3>🎉 A role-based Flask web application for managing academic operations in an educational institution</h3>

</div>

---

## 📖 Overview

**CMS (Academic Data Management System)** is a full-stack **Flask** web application for running the academic side of an institution — student records, staff-to-class allocation, attendance, Continuous Internal Evaluation (CIE) marks, and reporting — through three role-based dashboards: **Admin**, **HOD**, and **Staff**. Data is persisted in MySQL via Flask-SQLAlchemy, schema changes are tracked with Flask-Migrate/Alembic, and the system can generate PDF/Excel reports and scheduled database backups.

<table align="center">
<tr>
<td align="center">🏗️<br/><b>Architecture</b><br/>Flask Blueprints (Route → Service → Model)</td>
<td align="center">🔐<br/><b>Auth</b><br/>Flask-Login, 3 role authorities</td>
<td align="center">🗄️<br/><b>Data Layer</b><br/>SQLAlchemy ORM + Alembic migrations</td>
<td align="center">📊<br/><b>Reporting Layer</b><br/>ReportLab, fpdf2, pandas, openpyxl</td>
</tr>
</table>

## ✨ Features

<table align="center" width="100%">
<tr>
<td width="33%" valign="top">

### 🔐 Auth & Structure
- Role-based login (Admin, HOD, Staff)
- Flask-Login session management
- Manage students by branch & batch
- Manage class structures & subjects
- Maintenance mode toggle

</td>
<td width="33%" valign="top">

### 📝 Academic & CIE
- Staff-to-class & subject allocation
- Attendance entry & history tracking
- Configure CIE exam structures
- Manage CIE question papers
- Record & evaluate CIE marks

</td>
<td width="33%" valign="top">

### 📊 Reports & Backups
- PDF report generation (ReportLab/fpdf2)
- Excel data exports (pandas/openpyxl)
- Automated database backups
- Backup log audit history
- REST API for attendance & CIE data

</td>
</tr>
</table>

> 🔑 Access is enforced per Flask blueprint — `/admin`, `/hod`, `/staff`, and `/auth` routes are each guarded by role-based checks.

## 🛠️ Technology Stack

<div align="center">

![My Skills](https://skillicons.dev/icons?i=python,flask,mysql,html,css,js,bootstrap,git,vscode)

</div>

**Backend & Security:** Python 3.11 · Flask · Flask-Login · Cryptography
**ORM & Database:** Flask-SQLAlchemy · Flask-Migrate (Alembic) · MySQL (PyMySQL)
**Reporting & Templating:** ReportLab · fpdf2 · pandas · openpyxl · Jinja2

## 🏗️ Architecture & Workflow

```mermaid
flowchart TD
    A["🌐 Browser<br/>Admin / HOD / Staff"] -->|"HTTP Request"| B["🛡️ Flask-Login Guard<br/>(Blueprints: auth / admin / hod / staff)"]
    B --> C["🎮 Routes (Blueprints)<br/>auth_routes / admin_routes /<br/>hod_routes / staff_routes"]
    C --> D["⚙️ Service Layer<br/>attendance_service / cie_service / report_service"]
    C --> E["🗄️ SQLAlchemy ORM<br/>Models Layer"]
    D --> E
    E --> F[("🐬 MySQL<br/>academic_data_management")]
    F --> E
    E --> C
    C -->|"Model + Context"| G["🎨 Jinja2 Templates<br/>admin.html / hod.html / staff.html"]
    G -->|"Rendered HTML"| A

    style A fill:#0f0c29,stroke:#00d4ff,color:#ffffff
    style B fill:#1a1440,stroke:#ff4d6d,color:#ffffff
    style G fill:#0f0c29,stroke:#2cb67d,color:#ffffff
    style F fill:#1a1440,stroke:#7f5af0,color:#ffffff

Request flow: Requests flow through Flask blueprints scoped to a role. Routes call into the services layer for business logic, which operates on SQLAlchemy models. MySQL handles persistence, and Jinja2 renders role-appropriate templates.🚀 Installation & Setup1️⃣ Clone the RepositoryBashgit clone [https://github.com/YOUR_USERNAME/CMS.git](https://github.com/YOUR_USERNAME/CMS.git)
2️⃣ Navigate & Install DependenciesBashcd CMS
pip install -r requirements.txt
3️⃣ Configure Environment & DatabaseCreate a MySQL database named academic_data_management. Update your .env or config/config.py:PythonSQLALCHEMY_DATABASE_URI = "mysql+pymysql://YOUR_DB_USER:YOUR_DB_PASS@localhost/academic_data_management"
4️⃣ Run Migrations & Start AppBashflask db upgrade
flask run
5️⃣ Open Applicationhttp://localhost:5000
👤 Log in with your configured role credentials (Admin, HOD, or Staff) to access respective portal features.📂 Project StructureCMS/
├── api/                 → REST endpoints: attendance, CIE, backup, reports
├── config/              → config.py (DB URI, upload/backup folders)
├── models/              → SQLAlchemy models (User, Student, CIE, Attendance, etc.)
├── routes/              → Blueprints (auth, admin, hod, staff)
├── services/            → Business logic (auth, CIE, report, backup services)
├── templates/           → Jinja2 HTML templates
├── backups/             → Database & export backups
├── extensions.py        → db, login_manager initialization
├── app.py               → Flask application factory & entry point
├── database_schema.txt
└── README.md
🧩 Domain Model & Status FlowsModuleCore ModelsUsers & SecurityUser · Role · Control · MaintenanceModeAcademic HierarchyStudent · Batch · Branch · Class · Subject · StaffAllocationEvaluations & LogsAttendance · CIEConfig · CIEPapers · CIEMarks · BackupLogCore models encompass user authentication, multi-branch student academic structuring, evaluation tracking, and automated backup audit logs.ℹ️ API Note: CMS exposes both server-rendered views for role dashboards and REST endpoints under api/ for programmatic data exchange.🎯 Learning Outcomes🐍 Python 3.11 & Flask Architecture  •  🧩 Modular Blueprints  •  🗄️ SQLAlchemy ORM & Alembic  •  🔐 Flask-Login Auth  •  📊 PDF & Excel Generation  •  💾 Automated Backups🚀 Future Enhancements🤝 Contributing🍴 Fork the repository🌿 Create a feature branch💾 Commit your changes📤 Push your branch🔁 Submit a Pull Request🔗 Project Links📄 LicenseThis project is intended for educational and learning purposes. You are free to use, modify, and extend it for academic or personal projects.📝 Replace this section with a formal license (e.g. MIT, Apache 2.0) and add a LICENSE file if you plan to distribute this project publicly.⭐ SupportIf you found this project useful, please give it a ⭐ Star on GitHub — it encourages future improvements and helps others discover the project.
