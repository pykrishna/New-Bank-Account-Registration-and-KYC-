# 🏦 Ti Tans Bank KYC System - Visual Architecture Diagram

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           TI TANS BANK KYC SYSTEM                                  │
│                         Architecture Diagram                                       │
└─────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────┐                    ┌──────────────────┐
│   🌐 Web Browser │                    │   📱 Mobile      │
│   Streamlit UI   │                    │   Browser        │
│                  │                    │                  │
│  - Landing Page  │                    │  - Responsive UI │
│  - Login/Register│                    │  - Same Features │
│  - KYC Portal    │                    │                  │
│  - Dashboard     │                    │                  │
└────────┬─────────┘                    └────────┬─────────┘
         │                                        │
         │  HTTPS/HTTP                            │  HTTPS/HTTP
         │                                        │
         └──────────────┬─────────────────────────┘
                        │
                        ▼
         ┌──────────────────────────────────────┐
         │      🔀 Application Gateway           │
         │      Streamlit Application            │
         │      (app_main.py)                    │
         │                                       │
         │  - Route Management                   │
         │  - Session Control                    │
         │  - Request Handling                   │
         │  - View Navigation                    │
         └──────────────┬────────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│                    🏢 Backend Services Layer                                    │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐         │
│  │ 🔐 Authentication│  │ 📄 KYC Validation │  │ 🤖 AI Validation │         │
│  │    Service       │  │    Service       │  │    Service       │         │
│  │                  │  │                  │  │                  │         │
│  │ - User Register  │  │ - Photo Check    │  │ - Face Detection │         │
│  │ - Login/Logout   │  │ - Address Check  │  │ - Liveness Check │         │
│  │ - Password Hash  │  │ - Document Check │  │ - Quality Analysis│         │
│  │ - Session Mgmt   │  │ - Basic Scoring  │  │ - Face Matching  │         │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘         │
│                                                                               │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐         │
│  │ 📝 OCR Processing│  │ 👨‍💼 Admin Dashboard│  │ 📊 Audit Reports │         │
│  │    Service       │  │    Service       │  │    Service       │         │
│  │                  │  │                  │  │                  │         │
│  │ - Text Extract   │  │ - App Review     │  │ - Log Generation │         │
│  │ - PAN Validate   │  │ - Approve/Reject │  │ - Report Export  │         │
│  │ - Aadhar Validate│  │ - Fraud Alerts   │  │ - Compliance     │         │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘         │
│                                                                               │
└───────────────────────────────┬───────────────────────────────────────────────┘
                                │
                                │ Data Operations
                                │
                                ▼
         ┌──────────────────────────────────────┐
         │      💾 Database Storage               │
         │      PostgreSQL                        │
         │                                       │
         │  - users                              │
         │  - customers                          │
         │  - kyc_applications                   │
         │  - documents                          │
         │  - audit_logs                         │
         │  - notifications                      │
         └───────────────────────────────────────┘
                                │
                                │ File Storage
                                │
                                ▼
         ┌──────────────────────────────────────┐
         │      📁 File Storage System            │
         │      Local File System                │
         │                                       │
         │  - Document Files                     │
         │  - Photo Files                        │
         │  - submitted_data/documents/          │
         └──────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────────────────┐
│                    🔌 External Integrations                                    │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐         │
│  │ 🧠 GenAILab API  │  │ 📖 Tesseract OCR │  │ 👁️ OpenCV Library│         │
│  │                  │  │                  │  │                  │         │
│  │ - GPT-4 Vision   │  │ - Text Extract   │  │ - Face Detection │         │
│  │ - Liveness Check │  │ - Pattern Match  │  │ - Image Process  │         │
│  │ - AI Analysis    │  │ - Document Parse │  │ - Quality Check  │         │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘         │
│                                                                               │
└───────────────────────────────────────────────────────────────────────────────┘
```

---

## Component Descriptions

### 🌐 **User Interface Layer**

#### Web Browser (Streamlit UI)
- **Component**: Web-based user interface
- **Technology**: Streamlit 1.52.2, HTML5, CSS3
- **Features**:
  - Landing page with bank branding
  - User registration and login forms
  - KYC document upload portal
  - Customer dashboard for status tracking
  - Admin dashboard for management
  - Status check page (no login required)
- **Access**: HTTP/HTTPS via web browser

#### Mobile Browser
- **Component**: Mobile-responsive interface
- **Technology**: Responsive Streamlit UI
- **Features**: Same functionality as web, optimized for mobile devices

---

### 🔀 **Application Gateway**

#### Streamlit Application (app_main.py)
- **Component**: Main application controller
- **Technology**: Python, Streamlit Framework
- **Responsibilities**:
  - Request routing and view management
  - Session state management
  - User authentication flow control
  - Error handling and user feedback
  - Integration with all backend services
- **Key Features**:
  - Progressive KYC flow (first login redirect)
  - Role-based page access
  - Real-time status updates
  - File upload handling

---

### 🏢 **Backend Services Layer**

#### 🔐 Authentication Service
- **Component**: User authentication and authorization
- **File**: `db_helpers.py`
- **Technology**: Python, SHA-256 hashing
- **Functions**:
  - User registration with validation
  - Login authentication
  - Password hashing and verification
  - Session management
  - Duplicate prevention (username, email, PAN, Aadhar)

#### 📄 KYC Validation Service
- **Component**: Basic KYC validation logic
- **File**: `kyc_validator.py`
- **Technology**: Python, Image Processing
- **Functions**:
  - Photo validation (dimensions, file size, format)
  - Address validation (completeness, OCR matching)
  - Document validation (presence, verification status)
  - Weighted scoring calculation
  - Status determination

#### 🤖 AI Validation Service
- **Component**: Advanced AI-powered validation
- **File**: `ai_kyc_validator.py`
- **Technology**: OpenCV, GPT-4 Vision, NumPy
- **Functions**:
  - Face detection using OpenCV Haar Cascade
  - Liveness detection via GPT-4 Vision API
  - Image quality analysis (brightness, contrast, noise, sharpness)
  - Face matching between photo and ID document
  - Document type detection (PAN vs Aadhar)
  - Advanced scoring with AI features

#### 📝 OCR Processing Service
- **Component**: Document text extraction and validation
- **File**: `ocr_engine.py`
- **Technology**: Tesseract OCR, Python Regex
- **Functions**:
  - Text extraction from images (PAN, Aadhar)
  - Pattern matching for document formats
  - Field extraction (name, DOB, ID numbers, address)
  - Document completeness scoring
  - Fallback to mock OCR if Tesseract unavailable

#### 👨‍💼 Admin Dashboard Service
- **Component**: Administrative functions
- **File**: `admin_dashboard.py`
- **Technology**: Python, Streamlit
- **Functions**:
  - View pending KYC applications
  - Review customer documents and validation scores
  - Manual approve/reject actions
  - Fraud alert monitoring
  - System health metrics
  - Individual document rejection

#### 📊 Audit Reports Service
- **Component**: Audit trail and compliance reporting
- **File**: `audit_reports.py`
- **Technology**: Python, Pandas, OpenPyXL
- **Functions**:
  - Audit log generation and viewing
  - Report filtering (date range, action type)
  - CSV/Excel export functionality
  - Compliance-ready report generation

---

### 💾 **Data Storage Layer**

#### PostgreSQL Database
- **Component**: Relational database management system
- **Technology**: PostgreSQL 12+
- **Connection**: psycopg2-binary with connection pooling
- **Schema**:
  - **users**: User accounts and authentication data
  - **customers**: Customer profiles and KYC information
  - **kyc_applications**: KYC application records with validation scores
  - **documents**: Uploaded documents with OCR extracted data (JSONB)
  - **audit_logs**: Complete system audit trail
  - **notifications**: User notifications
- **Features**:
  - ACID compliance
  - Foreign key constraints
  - Indexes for performance
  - Triggers for automatic updates
  - JSONB for flexible OCR data storage

#### 📁 File Storage System
- **Component**: Local file system storage
- **Location**: `submitted_data/documents/`
- **Purpose**: Store uploaded documents and photos
- **Features**:
  - Secure file storage
  - File path tracking in database
  - Support for multiple formats (PDF, JPG, PNG)
  - File size validation

---

### 🔌 **External Integrations**

#### 🧠 GenAILab API (GPT-4 Vision)
- **Component**: AI-powered liveness detection
- **Technology**: OpenAI GPT-4 Vision via TCS GenAILab
- **Purpose**: Advanced photo liveness verification
- **Functions**:
  - Analyze images for liveness
  - Detect printed/screen photos
  - Return confidence scores
- **Integration**: Via `ai_helper.py`

#### 📖 Tesseract OCR
- **Component**: Optical Character Recognition engine
- **Technology**: Tesseract OCR Engine
- **Purpose**: Text extraction from document images
- **Functions**:
  - Extract text from images
  - Support multiple languages (English)
  - PDF to image conversion
- **Integration**: Via `ocr_engine.py`

#### 👁️ OpenCV Library
- **Component**: Computer vision library
- **Technology**: OpenCV 4.12.0
- **Purpose**: Image processing and face detection
- **Functions**:
  - Face detection (Haar Cascade Classifier)
  - Image quality analysis
  - Template matching for face comparison
  - Histogram comparison
- **Integration**: Via `ai_kyc_validator.py`

---

## 🔄 Data Flow Summary

### Registration Flow
```
User → Web Browser → Application Gateway → Authentication Service → Database
                                                                    ↓
                                                              User Created
                                                                    ↓
User ← Web Browser ← Application Gateway ← Authentication Service ← Database
```

### KYC Submission Flow
```
User → Upload Documents → Application Gateway → OCR Service → Tesseract OCR
                                                                    ↓
                                                              Text Extracted
                                                                    ↓
User → Submit KYC → Application Gateway → AI Validation Service → OpenCV + GenAILab
                                                                    ↓
                                                              Validation Complete
                                                                    ↓
User ← Notification ← Application Gateway ← AI Validation Service ← Database
```

### Admin Review Flow
```
Admin → Login → Application Gateway → Admin Service → Database
                                                          ↓
                                                    Fetch Applications
                                                          ↓
Admin → Approve/Reject → Application Gateway → Admin Service → Database
                                                                    ↓
                                                              Status Updated
                                                                    ↓
Admin ← Confirmation ← Application Gateway ← Admin Service ← Database
```

---

## 🎯 Key Architecture Features

### ✅ **Scalability**
- Connection pooling for efficient database access
- Stateless application design
- Modular service architecture
- Can scale horizontally with load balancer

### ✅ **Security**
- Password hashing (SHA-256)
- SQL injection prevention (parameterized queries)
- Session-based authentication
- Role-based access control
- Complete audit trail

### ✅ **Reliability**
- Transaction management
- Error handling and rollback
- Fallback mechanisms (mock OCR)
- Data validation at multiple layers

### ✅ **Maintainability**
- Clear separation of concerns
- Modular component design
- Comprehensive documentation
- Standard coding practices

---

## 📊 Technology Stack Summary

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Streamlit 1.52.2 | Web framework and UI |
| **Backend** | Python 3.8+ | Core programming language |
| **Database** | PostgreSQL 12+ | Data persistence |
| **Database Driver** | psycopg2-binary | Database connectivity |
| **AI/ML** | OpenCV 4.12.0 | Computer vision |
| **AI/ML** | GPT-4 Vision | Liveness detection |
| **OCR** | Tesseract OCR | Text extraction |
| **Image Processing** | Pillow, NumPy | Image manipulation |
| **Reporting** | Pandas, OpenPyXL | Data export |

---

**This visual architecture diagram provides a clear overview of all system components and their relationships! 🏗️✅**

