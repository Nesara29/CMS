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
- PDF report generation (ReportLab/fpdf2)[cite: 2]
- Excel data exports (pandas/openpyxl)[cite: 2]
- Automated database backups[cite: 2]
- Backup log audit history[cite: 2]
- REST API for attendance & CIE data[cite: 2]

</td>
</tr>
</table>

> 🔑 Access is enforced per Flask blueprint — `/admin`, `/hod`, `/staff`, and `/auth` routes are each guarded by role-based checks[cite: 2].

## 🛠️ Technology Stack

<div align="center">

![My Skills](https://skillicons.dev/icons?i=python,flask,mysql,html,css,js,bootstrap,git,vscode)

</div>

**Backend & Security:** Python 3.11 · Flask · Flask-Login · Cryptography[cite: 2]
**ORM & Database:** Flask-SQLAlchemy · Flask-Migrate (Alembic) · MySQL (PyMySQL)[cite: 2]
**Reporting & Templating:** ReportLab · fpdf2 · pandas · openpyxl · Jinja2[cite: 2]

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
