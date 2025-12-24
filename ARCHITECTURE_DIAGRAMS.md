# 🏗️ Ti Tans Bank KYC System - Architecture Diagrams

## System Architecture Overview

This document provides comprehensive architecture diagrams for the Ti Tans Bank KYC Portal system, showing component interactions, data flow, and technology stack.

---

## 📊 High-Level System Architecture

```mermaid
graph TB
    subgraph "User Interface Layer"
        WEB[Web Browser<br/>Streamlit UI]
        MOBILE[Mobile Browser<br/>Responsive UI]
    end
    
    subgraph "Application Gateway"
        APP[Streamlit Application<br/>app_main.py]
    end
    
    subgraph "Business Logic Layer"
        AUTH[Authentication Service<br/>db_helpers.py]
        KYC[KYC Validation Engine<br/>kyc_validator.py]
        AI[AI Validation Service<br/>ai_kyc_validator.py]
        OCR[OCR Processing Service<br/>ocr_engine.py]
        ADMIN[Admin Dashboard<br/>admin_dashboard.py]
        AUDIT[Audit & Reporting<br/>audit_reports.py]
    end
    
    subgraph "Data Layer"
        DB[(PostgreSQL Database<br/>horizon_bank_kyc)]
        FS[File Storage<br/>submitted_data/documents]
    end
    
    subgraph "External Services"
        GENAI[GenAILab API<br/>GPT-4 Vision]
        TESS[Tesseract OCR<br/>Text Extraction]
        OPENCV[OpenCV<br/>Face Detection]
    end
    
    WEB -->|HTTP/HTTPS| APP
    MOBILE -->|HTTP/HTTPS| APP
    
    APP -->|Session Management| AUTH
    APP -->|Document Upload| OCR
    APP -->|Validation Request| KYC
    APP -->|Admin Access| ADMIN
    APP -->|Reports| AUDIT
    
    AUTH -->|User Verification| DB
    KYC -->|Validation Logic| AI
    AI -->|Face Detection| OPENCV
    AI -->|Liveness Check| GENAI
    OCR -->|Text Extraction| TESS
    OCR -->|Store Results| DB
    
    KYC -->|Save Status| DB
    AI -->|Save Scores| DB
    ADMIN -->|Query Data| DB
    AUDIT -->|Export Reports| DB
    
    APP -->|Store Files| FS
    OCR -->|Read Files| FS
    AI -->|Read Files| FS
```

---

## 🎯 Component Architecture Diagram

```mermaid
graph LR
    subgraph "Frontend Layer"
        UI[Streamlit Web Interface<br/>- Landing Page<br/>- Login/Register<br/>- KYC Portal<br/>- Dashboard<br/>- Admin Panel]
    end
    
    subgraph "Application Layer"
        ROUTER[Route Handler<br/>app_main.py<br/>- View Management<br/>- Session Control]
        STYLING[UI Styling<br/>styling.py<br/>- CSS Themes<br/>- Glassmorphism]
    end
    
    subgraph "Service Layer"
        AUTH_SVC[Authentication Service<br/>db_helpers.py<br/>- User Registration<br/>- Login/Logout<br/>- Password Hashing]
        
        KYC_SVC[KYC Service<br/>kyc_validator.py<br/>- Basic Validation<br/>- Address Check<br/>- Document Check]
        
        AI_SVC[AI Validation Service<br/>ai_kyc_validator.py<br/>- Face Detection<br/>- Liveness Check<br/>- Quality Analysis<br/>- Face Matching]
        
        OCR_SVC[OCR Service<br/>ocr_engine.py<br/>- Text Extraction<br/>- PAN Validation<br/>- Aadhar Validation]
        
        ADMIN_SVC[Admin Service<br/>admin_dashboard.py<br/>- Application Review<br/>- Approve/Reject<br/>- Fraud Alerts]
        
        AUDIT_SVC[Audit Service<br/>audit_reports.py<br/>- Log Generation<br/>- Report Export]
    end
    
    subgraph "Data Access Layer"
        DB_CONFIG[Database Config<br/>database_config.py<br/>- Connection Pooling<br/>- Query Execution]
        
        DB_HELPERS[Database Helpers<br/>db_helpers.py<br/>- CRUD Operations<br/>- Data Validation]
    end
    
    subgraph "Data Storage"
        POSTGRES[(PostgreSQL<br/>- users<br/>- customers<br/>- kyc_applications<br/>- documents<br/>- audit_logs)]
        
        FILES[File System<br/>- Document Storage<br/>- Photo Storage]
    end
    
    subgraph "External APIs"
        GENAI_API[GenAILab API<br/>- GPT-4 Vision<br/>- Liveness Detection]
        
        OCR_ENGINE[Tesseract OCR<br/>- Text Extraction<br/>- Pattern Matching]
        
        CV_LIB[OpenCV Library<br/>- Face Detection<br/>- Image Processing]
    end
    
    UI --> ROUTER
    ROUTER --> STYLING
    ROUTER --> AUTH_SVC
    ROUTER --> KYC_SVC
    ROUTER --> AI_SVC
    ROUTER --> OCR_SVC
    ROUTER --> ADMIN_SVC
    ROUTER --> AUDIT_SVC
    
    AUTH_SVC --> DB_HELPERS
    KYC_SVC --> DB_HELPERS
    AI_SVC --> DB_HELPERS
    OCR_SVC --> DB_HELPERS
    ADMIN_SVC --> DB_HELPERS
    AUDIT_SVC --> DB_HELPERS
    
    DB_HELPERS --> DB_CONFIG
    DB_CONFIG --> POSTGRES
    
    OCR_SVC --> OCR_ENGINE
    OCR_SVC --> FILES
    
    AI_SVC --> CV_LIB
    AI_SVC --> GENAI_API
    AI_SVC --> FILES
    
    KYC_SVC --> FILES
```

---

## 🔄 Data Flow Architecture

```mermaid
sequenceDiagram
    participant User
    participant UI as Streamlit UI
    participant Auth as Auth Service
    participant DB as PostgreSQL
    participant OCR as OCR Engine
    participant AI as AI Validator
    participant Ext as External APIs
    
    User->>UI: Register Account
    UI->>Auth: create_user()
    Auth->>DB: INSERT INTO users
    Auth->>DB: INSERT INTO customers
    DB-->>Auth: user_id, customer_id
    Auth-->>UI: Registration Success
    UI-->>User: Account Created
    
    User->>UI: Login
    UI->>Auth: authenticate_user()
    Auth->>DB: SELECT user WHERE username
    DB-->>Auth: user_data
    Auth->>Auth: verify_password()
    Auth->>DB: UPDATE last_login
    Auth-->>UI: Authentication Success
    UI-->>User: Redirect to KYC Portal
    
    User->>UI: Upload Documents
    UI->>OCR: extract_text()
    OCR->>Ext: Tesseract OCR
    Ext-->>OCR: Extracted Text
    OCR->>OCR: validate_pan() / validate_aadhar()
    OCR-->>UI: OCR Results
    UI->>DB: INSERT INTO documents
    UI->>DB: Save file_path, ocr_data
    DB-->>UI: document_id
    
    User->>UI: Submit KYC
    UI->>AI: perform_advanced_kyc_validation()
    AI->>DB: Get customer data
    AI->>DB: Get documents
    AI->>AI: detect_face_in_image()
    AI->>Ext: OpenCV Face Detection
    Ext-->>AI: Face Detection Results
    AI->>AI: detect_liveness()
    AI->>Ext: GPT-4 Vision API
    Ext-->>AI: Liveness Results
    AI->>AI: compare_faces()
    AI->>AI: analyze_image_quality()
    AI->>AI: Calculate weighted scores
    AI->>DB: UPDATE kyc_applications
    AI->>DB: UPDATE documents
    AI->>DB: UPDATE customers
    AI-->>UI: Validation Results
    UI-->>User: Status Notification
```

---

## 🗄️ Database Architecture

```mermaid
erDiagram
    USERS ||--o{ CUSTOMERS : "has"
    CUSTOMERS ||--o{ KYC_APPLICATIONS : "submits"
    KYC_APPLICATIONS ||--o{ DOCUMENTS : "contains"
    USERS ||--o{ AUDIT_LOGS : "generates"
    CUSTOMERS ||--o{ NOTIFICATIONS : "receives"
    KYC_APPLICATIONS ||--o{ AUDIT_LOGS : "tracks"
    
    USERS {
        uuid user_id PK
        string username UK
        string email UK
        string password_hash
        string role
        boolean is_active
        timestamp created_at
        timestamp last_login
    }
    
    CUSTOMERS {
        uuid customer_id PK
        uuid user_id FK
        string first_name
        string last_name
        string full_name
        date date_of_birth
        string gender
        string address
        string city_town
        string pincode
        string pan_card
        string aadhar_no
        string phone_number
        string kyc_status
        text photo_path
        timestamp created_at
    }
    
    KYC_APPLICATIONS {
        uuid application_id PK
        uuid customer_id FK
        string application_status
        decimal overall_score
        text notes
        text rejection_reason
        timestamp submission_date
        timestamp verification_date
        uuid verified_by FK
    }
    
    DOCUMENTS {
        uuid document_id PK
        uuid application_id FK
        string document_type
        string document_name
        text file_path
        bigint file_size
        string mime_type
        jsonb ocr_extracted_data
        string verification_status
        text verification_notes
        timestamp created_at
        timestamp verified_at
    }
    
    AUDIT_LOGS {
        uuid log_id PK
        uuid user_id FK
        string action_type
        string entity_type
        uuid entity_id
        text description
        string ip_address
        timestamp created_at
    }
    
    NOTIFICATIONS {
        uuid notification_id PK
        uuid customer_id FK
        string notification_type
        string title
        text message
        boolean is_read
        timestamp created_at
    }
```

---

## 🤖 AI/ML Processing Architecture

```mermaid
graph TD
    subgraph "Input Layer"
        PHOTO[Customer Photo]
        ID_DOC[ID Document<br/>PAN/Aadhar]
    end
    
    subgraph "Image Processing"
        PREPROC[Image Preprocessing<br/>- Format Conversion<br/>- Resize<br/>- Normalize]
    end
    
    subgraph "AI Validation Pipeline"
        FACE[Face Detection<br/>OpenCV Haar Cascade<br/>- Face Count<br/>- Face Position<br/>- Face Size]
        
        LIVE[Liveness Detection<br/>GPT-4 Vision + Image Analysis<br/>- Sharpness Check<br/>- Color Depth<br/>- Resolution<br/>- EXIF Data]
        
        QUALITY[Quality Analysis<br/>OpenCV + NumPy<br/>- Brightness<br/>- Contrast<br/>- Noise Level<br/>- Edge Density]
        
        MATCH[Face Matching<br/>Template Matching + Histogram<br/>- Photo vs ID Photo<br/>- Similarity Score]
    end
    
    subgraph "OCR Pipeline"
        OCR_EXTRACT[Text Extraction<br/>Tesseract OCR<br/>- Raw Text Output]
        
        OCR_VALIDATE[Document Validation<br/>Pattern Matching<br/>- PAN Format<br/>- Aadhar Format<br/>- Name Extraction]
    end
    
    subgraph "Scoring Engine"
        SCORE[Weighted Scoring<br/>- Photo: 40%<br/>- Address: 15%<br/>- ID Doc: 30%<br/>- Photo Doc: 15%]
        
        DECISION[Decision Engine<br/>- Critical Issues Check<br/>- Threshold Comparison<br/>- Status Determination]
    end
    
    PHOTO --> PREPROC
    ID_DOC --> PREPROC
    
    PREPROC --> FACE
    PREPROC --> LIVE
    PREPROC --> QUALITY
    PREPROC --> MATCH
    
    ID_DOC --> OCR_EXTRACT
    OCR_EXTRACT --> OCR_VALIDATE
    
    FACE --> SCORE
    LIVE --> SCORE
    QUALITY --> SCORE
    MATCH --> SCORE
    OCR_VALIDATE --> SCORE
    
    SCORE --> DECISION
    DECISION --> RESULT[Validation Result<br/>- Approved/Rejected<br/>- Score Breakdown<br/>- Issues List]
```

---

## 🔐 Security Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        CLIENT[Web Browser<br/>HTTPS Connection]
    end
    
    subgraph "Application Security"
        SESSION[Session Management<br/>Streamlit Session State<br/>- Authentication Status<br/>- User Data<br/>- Role-based Access]
        
        AUTH_CHECK[Authentication Check<br/>- Password Hashing SHA-256<br/>- Session Validation<br/>- Role Verification]
        
        INPUT_VAL[Input Validation<br/>- SQL Injection Prevention<br/>- XSS Prevention<br/>- File Type Validation<br/>- File Size Limits]
    end
    
    subgraph "Data Security"
        DB_SEC[Database Security<br/>- Parameterized Queries<br/>- Connection Pooling<br/>- Transaction Management]
        
        FILE_SEC[File Security<br/>- Secure File Storage<br/>- Access Control<br/>- File Validation]
        
        AUDIT[Audit Trail<br/>- All Actions Logged<br/>- IP Address Tracking<br/>- Timestamp Recording]
    end
    
    subgraph "External Security"
        API_SEC[API Security<br/>- GenAILab API Key<br/>- HTTPS Only<br/>- Request Validation]
    end
    
    CLIENT -->|HTTPS| SESSION
    SESSION --> AUTH_CHECK
    AUTH_CHECK --> INPUT_VAL
    INPUT_VAL --> DB_SEC
    INPUT_VAL --> FILE_SEC
    AUTH_CHECK --> AUDIT
    INPUT_VAL --> API_SEC
```

---

## 📦 Technology Stack Architecture

```mermaid
graph TB
    subgraph "Frontend Technologies"
        STREAMLIT[Streamlit 1.52.2<br/>Web Framework]
        CSS[Custom CSS<br/>Glassmorphism Design]
        HTML[HTML5<br/>Responsive UI]
    end
    
    subgraph "Backend Technologies"
        PYTHON[Python 3.8+<br/>Core Language]
        ASYNC[Async Processing<br/>Background Tasks]
    end
    
    subgraph "Database Technologies"
        POSTGRES[PostgreSQL 12+<br/>Relational Database]
        PSYCOPG2[psycopg2-binary<br/>Database Adapter]
        JSONB[JSONB<br/>Flexible Data Storage]
    end
    
    subgraph "AI/ML Technologies"
        OPENCV[OpenCV 4.12.0<br/>Computer Vision]
        NUMPY[NumPy 2.2.6<br/>Numerical Computing]
        PILLOW[Pillow 12.0<br/>Image Processing]
        OPENAI[OpenAI 2.14.0<br/>GPT-4 Vision API]
        TESSERACT[Tesseract OCR<br/>Text Extraction]
    end
    
    subgraph "Utility Libraries"
        PANDAS[Pandas 2.3.3<br/>Data Manipulation]
        OPENPYXL[OpenPyXL<br/>Excel Export]
        DOTENV[python-dotenv<br/>Environment Variables]
    end
    
    STREAMLIT --> PYTHON
    CSS --> STREAMLIT
    HTML --> STREAMLIT
    
    PYTHON --> PSYCOPG2
    PSYCOPG2 --> POSTGRES
    
    PYTHON --> OPENCV
    PYTHON --> NUMPY
    PYTHON --> PILLOW
    PYTHON --> OPENAI
    PYTHON --> TESSERACT
    
    PYTHON --> PANDAS
    PYTHON --> OPENPYXL
    PYTHON --> DOTENV
```

---

## 🎯 Component Descriptions

### 1. **User Interface Layer**

#### Web Browser (Streamlit UI)
- **Technology**: Streamlit 1.52.2
- **Purpose**: Provides web-based user interface for all system interactions
- **Features**:
  - Responsive design for desktop and mobile browsers
  - Glassmorphism UI with custom CSS styling
  - Page-specific color schemes
  - Real-time status updates
- **Components**:
  - Landing Page
  - Login/Registration Forms
  - KYC Portal (Document Upload)
  - Customer Dashboard
  - Admin Dashboard
  - Status Check Page

---

### 2. **Application Gateway**

#### Streamlit Application (app_main.py)
- **Technology**: Python, Streamlit
- **Purpose**: Main application entry point and routing controller
- **Responsibilities**:
  - View/page routing and navigation
  - Session state management
  - User authentication flow
  - Request handling and response generation
  - Error handling and user feedback
- **Key Functions**:
  - `change_view()`: Navigate between pages
  - `handle_webcam_capture()`: Camera integration
  - `_display_application_details()`: Status display

---

### 3. **Business Logic Layer**

#### Authentication Service (db_helpers.py)
- **Technology**: Python, SHA-256 hashing
- **Purpose**: User authentication and authorization
- **Features**:
  - User registration with duplicate prevention
  - Password hashing (SHA-256)
  - Session management
  - Role-based access control (customer/admin)
- **Key Functions**:
  - `create_user()`: Register new user
  - `authenticate_user()`: Login validation
  - `hash_password()`: Secure password storage

#### KYC Validation Service (kyc_validator.py)
- **Technology**: Python, Image Processing
- **Purpose**: Basic KYC validation logic
- **Features**:
  - Photo validation (dimensions, file size)
  - Address validation (completeness, OCR matching)
  - Document validation (presence, verification status)
  - Weighted scoring calculation
- **Key Functions**:
  - `validate_photo()`: Photo quality checks
  - `validate_address()`: Address validation
  - `perform_kyc_validation()`: Overall validation

#### AI Validation Service (ai_kyc_validator.py)
- **Technology**: OpenCV, GPT-4 Vision, NumPy
- **Purpose**: Advanced AI-powered validation
- **Features**:
  - Face detection using OpenCV Haar Cascade
  - Liveness detection via GPT-4 Vision API
  - Image quality analysis (brightness, contrast, noise)
  - Face matching between photo and ID document
  - Document type detection (PAN vs Aadhar)
- **Key Functions**:
  - `detect_face_in_image()`: Face detection
  - `detect_liveness()`: Liveness verification
  - `compare_faces()`: Face matching
  - `perform_advanced_kyc_validation()`: Complete AI validation

#### OCR Processing Service (ocr_engine.py)
- **Technology**: Tesseract OCR, Python Regex
- **Purpose**: Text extraction and document validation
- **Features**:
  - Text extraction from images (PAN, Aadhar)
  - Pattern matching for document formats
  - Field extraction (name, DOB, ID numbers)
  - Completeness scoring
- **Key Functions**:
  - `extract_text_from_image()`: OCR text extraction
  - `validate_pan()`: PAN card validation
  - `validate_aadhar()`: Aadhar card validation

#### Admin Dashboard Service (admin_dashboard.py)
- **Technology**: Python, Streamlit
- **Purpose**: Administrative functions and customer management
- **Features**:
  - Pending application review
  - Manual approve/reject actions
  - Fraud alert monitoring
  - System health metrics
  - Application details view
- **Key Functions**:
  - `get_pending_applications()`: Fetch pending apps
  - `admin_approve_kyc()`: Manual approval
  - `admin_reject_kyc()`: Manual rejection

#### Audit & Reporting Service (audit_reports.py)
- **Technology**: Python, Pandas, OpenPyXL
- **Purpose**: Audit trail and compliance reporting
- **Features**:
  - Audit log generation
  - Report filtering (date, action type)
  - CSV/Excel export
  - Compliance-ready reports
- **Key Functions**:
  - `get_audit_logs()`: Retrieve audit logs
  - `export_to_csv()`: CSV export
  - `export_to_excel()`: Excel export

---

### 4. **Data Access Layer**

#### Database Configuration (database_config.py)
- **Technology**: psycopg2-binary, PostgreSQL
- **Purpose**: Database connection management
- **Features**:
  - Connection pooling (1-10 connections)
  - Context manager for safe connections
  - Automatic transaction management
  - Error handling and rollback
- **Key Functions**:
  - `create_connection_pool()`: Initialize pool
  - `get_connection()`: Get connection from pool
  - `execute_query()`: Execute SQL queries

#### Database Helpers (db_helpers.py)
- **Technology**: Python, PostgreSQL
- **Purpose**: Database CRUD operations
- **Features**:
  - User management operations
  - Customer profile operations
  - KYC application operations
  - Document operations
  - Audit logging
- **Key Functions**:
  - `create_customer()`: Create customer record
  - `create_kyc_application()`: Create KYC app
  - `save_document()`: Save document metadata
  - `log_audit()`: Log system actions

---

### 5. **Data Storage Layer**

#### PostgreSQL Database
- **Technology**: PostgreSQL 12+
- **Purpose**: Persistent data storage
- **Schema**:
  - `users`: User accounts and authentication
  - `customers`: Customer profiles and KYC data
  - `kyc_applications`: KYC application records
  - `documents`: Uploaded documents with OCR data
  - `audit_logs`: System audit trail
  - `notifications`: User notifications
- **Features**:
  - ACID compliance
  - JSONB for flexible OCR data storage
  - Foreign key constraints
  - Indexes for performance
  - Triggers for automatic updates

#### File Storage System
- **Technology**: Local file system
- **Purpose**: Document and photo storage
- **Location**: `submitted_data/documents/`
- **Features**:
  - Secure file storage
  - File path tracking in database
  - Support for multiple formats (PDF, JPG, PNG)
  - File size validation

---

### 6. **External Services**

#### GenAILab API (GPT-4 Vision)
- **Technology**: OpenAI API, TCS GenAILab
- **Purpose**: Advanced liveness detection
- **Features**:
  - Image analysis for liveness
  - Detection of printed/screen photos
  - JSON response parsing
  - Error handling and fallback
- **Integration**: Via `ai_helper.py`

#### Tesseract OCR
- **Technology**: Tesseract OCR Engine
- **Purpose**: Text extraction from documents
- **Features**:
  - Multi-language support (English)
  - PDF to image conversion
  - Pattern matching for document types
  - Fallback to mock OCR if unavailable
- **Integration**: Via `ocr_engine.py`

#### OpenCV Library
- **Technology**: OpenCV 4.12.0
- **Purpose**: Computer vision and image processing
- **Features**:
  - Face detection (Haar Cascade)
  - Image quality analysis
  - Template matching
  - Histogram comparison
- **Integration**: Via `ai_kyc_validator.py`

---

## 🔄 System Flow Summary

### Registration Flow
1. User accesses web interface
2. Fills registration form
3. System validates input and checks duplicates
4. Creates user account and customer profile
5. Stores data in PostgreSQL
6. Redirects to login

### KYC Submission Flow
1. User logs in (first login → KYC Portal)
2. Uploads photo (camera or file)
3. Uploads ID document (PAN/Aadhar)
4. OCR extracts text from document
5. AI validates photo (face, liveness, quality)
6. AI matches faces (photo vs ID)
7. System calculates weighted scores
8. Updates application status
9. Sends notification to user

### Admin Review Flow
1. Admin logs in
2. Views pending applications
3. Reviews documents and validation scores
4. Approves or rejects application
5. Updates status in database
6. Logs audit trail
7. Customer receives notification

---

## 📊 Architecture Characteristics

### Scalability
- Connection pooling for database efficiency
- Stateless application design
- File storage can be migrated to cloud storage
- Horizontal scaling possible with load balancer

### Security
- Password hashing (SHA-256)
- SQL injection prevention (parameterized queries)
- Session-based authentication
- Role-based access control
- Complete audit trail

### Reliability
- Transaction management
- Error handling and rollback
- Fallback mechanisms (mock OCR)
- Data validation at multiple layers

### Maintainability
- Modular architecture
- Separation of concerns
- Clear component boundaries
- Comprehensive documentation

---

## 🚀 Deployment Architecture

```
┌─────────────────────────────────────────┐
│         Production Environment          │
├─────────────────────────────────────────┤
│                                         │
│  ┌──────────────┐    ┌──────────────┐  │
│  │   Web App    │    │   Database   │  │
│  │  Streamlit   │◄──►│  PostgreSQL  │  │
│  │  Port 8501   │    │  Port 5432   │  │
│  └──────────────┘    └──────────────┘  │
│         │                    │          │
│         │                    │          │
│  ┌──────▼────────────────────▼──────┐  │
│  │      File Storage System          │  │
│  │   submitted_data/documents/       │  │
│  └──────────────────────────────────┘  │
│                                         │
│  ┌──────────────────────────────────┐   │
│  │    External APIs                 │   │
│  │  - GenAILab (HTTPS)              │   │
│  │  - Tesseract (Local)             │   │
│  └──────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

---

**This architecture diagram provides a complete view of the Ti Tans Bank KYC System components, their interactions, and technology stack! 🏗️✅**

