# Bella Vista Salon — User Stories

### 1. View Available Times — Must Have

**As a** salon client,  
**I want** to see available appointment times for an upcoming date,  
**so that** I can choose a convenient time.

**Acceptance Criteria:**
- **Given** I select a date from today through 90 days in the future, **when** time slots are available, **then** the system shows the available times for that date.
- **Given** I select a date outside the allowed range or before today, **when** I submit my selection, **then** the system rejects the date and asks me to select a valid date.
- **Given** all valid time slots for the selected date are booked or blocked, **when** I select the date, **then** the system says no times are available.

### 2. Book an Appointment — Must Have

**As a** salon client,  
**I want** to book an available service and time,  
**so that** I can schedule my visit.

**Acceptance Criteria:**
- **Given** I select an available service, date, and time, **when** I enter my full name, phone number or email address, and all other required information, **then** my appointment is confirmed.
- **Given** required information is missing or invalid, **including** full name, a valid phone number or email address, service, date, or time, **when** I submit the booking, **then** the system shows the relevant error and does not create the appointment.
- **Given** I select a valid date and time, **when** that time becomes unavailable before submission, **then** the system prevents the booking and asks me to choose another time.

### 3. View My Appointments — Must Have

**As a** salon client,  
**I want** to see my upcoming appointments,  
**so that** I can remember my schedule.

**Acceptance Criteria:**
- **Given** I am signed in and have an upcoming appointment, **when** I open my appointments, **then** the system displays only my appointment details.
- **Given** I am signed in and have no upcoming appointments, **when** I open the page, **then** the system shows that no appointments are scheduled.
- **Given** I am not signed in, **when** I open my appointments, **then** the system asks me to sign in.

### 4. Cancel an Appointment — Should Have

**As a** salon client,  
**I want** to cancel an upcoming appointment that belongs to me,  
**so that** I can cancel when I am unavailable.

**Acceptance Criteria:**
- **Given** I am signed in and viewing my own upcoming appointment, **when** I confirm cancellation, **then** the appointment is marked cancelled.
- **Given** I try to cancel another client's appointment or an appointment I do not own, **when** I submit the cancellation, **then** the system rejects the action.
- **Given** the appointment is already cancelled or completed, **when** I try to cancel it again, **then** the system does not create another cancellation.

### 5. View Daily Schedule — Must Have

**As a** salon staff member,  
**I want** to view the daily appointments for a selected date,  
**so that** I can manage the salon schedule.

**Acceptance Criteria:**
- **Given** I am authenticated as authorized staff and appointments exist on the selected date, **when** I open that date, **then** the appointments are displayed.
- **Given** I am authenticated as authorized staff and no appointments exist on the selected date, **when** I open that date, **then** the system shows that there are no appointments.
- **Given** I am not authorized staff, **when** I try to view the staff schedule, **then** the system rejects the action.

### 6. Update Appointment Status — Must Have

**As an** authorized salon staff member,  
**I want** to update an appointment's status,  
**so that** the schedule shows current information.

**Acceptance Criteria:**
- **Given** I am authenticated as authorized staff, **when** I change an appointment status to **Booked**, **Checked In**, **Completed**, or **Cancelled**, **then** the new status is saved.
- **Given** I try to change an appointment to an unrecognized status, **when** I submit the change, **then** the system rejects the change.
- **Given** I am not authenticated or not authorized staff, **when** I try to change a status, **then** the system rejects the action.

### 7. Block an Unavailable Time — Should Have

**As a** salon staff member,  
**I want** to block an unavailable time,  
**so that** clients cannot book when the salon is unavailable.

**Acceptance Criteria:**
- **Given** I am authenticated as authorized staff and the time is available, **when** staff block it, **then** it is removed from available times.
- **Given** I am authenticated as authorized staff and an appointment already exists at that time, **when** staff try to block it, **then** the system warns staff and does not remove the appointment.
- **Given** I am not authorized staff, **when** I try to block a time, **then** the system rejects the action.

### 8. Change an Appointment — Could Have

**As a** salon client,  
**I want** to change my own appointment time,  
**so that** I can adjust my schedule.

**Acceptance Criteria:**
- **Given** I am signed in and the appointment belongs to me, **when** I select an available time on a date within today through 90 days from today, **then** my appointment is moved.
- **Given** I am signed in and the appointment belongs to me, **when** I select a date outside the allowed range or a time that is already booked or blocked, **then** the system prevents the change.
- **Given** I try to change another client's appointment or an appointment I do not own, **when** I submit the change, **then** the system rejects the action.

## Priority Summary

| Priority | Stories |
|---|---|
| Must Have | 1, 2, 3, 5, 6 |
| Should Have | 4, 7 |
| Could Have | 8 |
