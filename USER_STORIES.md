# Bella Vista Salon — User Stories

### 1. View Available Times — Must Have

**As a** salon client,  
**I want** to see available appointment times,  
**so that** I can choose a convenient time.

**Acceptance Criteria:**
- **Given** I select a date, **when** times are available, **then** the system shows the available times.
- **Given** all times are booked, **when** I select the date, **then** the system says no times are available.

### 2. Book an Appointment — Must Have

**As a** salon client,  
**I want** to book an available service and time,  
**so that** I can schedule my visit.

**Acceptance Criteria:**
- **Given** I select an available service and time, **when** I enter the required information, **then** my appointment is confirmed.
- **Given** required information is missing, **when** I submit the booking, **then** the system shows an error and does not create the appointment.

### 3. View My Appointments — Must Have

**As a** salon client,  
**I want** to see my upcoming appointments,  
**so that** I can remember my schedule.

**Acceptance Criteria:**
- **Given** I have an upcoming appointment, **when** I open my appointments, **then** the appointment details are displayed.
- **Given** I have no upcoming appointments, **when** I open the page, **then** the system shows that no appointments are scheduled.

### 4. Cancel an Appointment — Should Have

**As a** salon client,  
**I want** to cancel an upcoming appointment,  
**so that** I can cancel when I am unavailable.

**Acceptance Criteria:**
- **Given** I have an upcoming appointment, **when** I confirm cancellation, **then** the appointment is marked cancelled.
- **Given** the appointment is already cancelled, **when** I try to cancel it again, **then** the system does not create another cancellation.

### 5. View Daily Schedule — Must Have

**As a** salon staff member,  
**I want** to view daily appointments,  
**so that** I can manage the salon schedule.

**Acceptance Criteria:**
- **Given** appointments exist, **when** I open the selected date, **then** the appointments are displayed.
- **Given** there are no appointments, **when** I open the schedule, **then** the system shows that there are no appointments.

### 6. Update Appointment Status — Must Have

**As a** salon staff member,  
**I want** to update an appointment's status,  
**so that** the schedule shows current information.

**Acceptance Criteria:**
- **Given** I am authorized staff, **when** I change the status, **then** the new status is saved.
- **Given** I am not authorized staff, **when** I try to change the status, **then** the system rejects the action.

### 7. Block an Unavailable Time — Should Have

**As a** salon staff member,  
**I want** to block an unavailable time,  
**so that** clients cannot book when the salon is unavailable.

**Acceptance Criteria:**
- **Given** the time is available, **when** staff block it, **then** it is removed from available times.
- **Given** an appointment already exists at that time, **when** staff try to block it, **then** the system warns staff and does not remove the appointment.

### 8. Change an Appointment — Could Have

**As a** salon client,  
**I want** to change my appointment time,  
**so that** I can adjust my schedule.

**Acceptance Criteria:**
- **Given** the new time is available, **when** I select it, **then** my appointment is moved.
- **Given** the new time is already booked, **when** I select it, **then** the system prevents the change.

## Priority Summary

| Priority | Stories |
|---|---|
| Must Have | 1, 2, 3, 5, 6 |
| Should Have | 4, 7 |
| Could Have | 8 |
