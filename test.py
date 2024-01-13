import streamlit as st

# Function definition here (as provided earlier)
def calculate_attendance(total_classes, classes_attended, desired_percentage):
    """
    Calculate the current attendance percentage and determine the number of classes
    to attend or miss to reach the desired attendance percentage.
    """
    # Current attendance percentage
    current_percentage = (classes_attended / total_classes) * 100 if total_classes else 0

    # Initialize variables for results
    classes_to_attend = 0
    classes_to_miss = 0

    # If current percentage is less than desired, calculate classes to attend
    if current_percentage < desired_percentage:
        # Required total attendance to reach desired percentage
        required_attendance = (desired_percentage / 100) * total_classes
        # Calculate the number of classes to attend to reach the desired percentage
        classes_to_attend = required_attendance - classes_attended
    elif current_percentage > desired_percentage:
        # Over-attendance scenario, calculate classes that can be missed
        max_attended_classes = (desired_percentage / 100) * total_classes
        classes_to_miss = classes_attended - max_attended_classes

    return current_percentage, classes_to_attend, classes_to_miss


# Streamlit application
def main():
    st.title("Attendance Management Calculator")

    total_classes = st.number_input("Enter Total Number of Classes Conducted", min_value=0)
    classes_attended = st.number_input("Enter Number of Classes Attended", min_value=0, max_value=total_classes)
    desired_percentage = st.slider("Enter Desired Attendance Percentage", min_value=0.0, max_value=100.0,step=0.5)

    current = st.empty()
    status = st.empty()

    future_classes = st.number_input("Enter Number of Future Classes", min_value=0)


    if st.button("Calculate"):
        current_percentage, classes_to_attend, classes_to_miss = calculate_attendance(total_classes, classes_attended, desired_percentage)
        current.success(f"Your current attendance percentage is {current_percentage:.2f}%")
        
        # Display different messages based on attendance scenario
        if classes_to_attend > 0:
            status.warning(f"You need to attend {classes_to_attend} more classes to reach your desired attendance percentage.")
        elif classes_to_miss > 0:
            status.success(f"You can miss up to {classes_to_miss:.0f} classes and still maintain your desired attendance percentage.")
        else:
            status.success("You are already at your desired attendance percentage.")

        plot = st.empty()

    
        future_attendance = future_classes - classes_to_miss if future_classes else 0

        plot_attendance_growth(total_classes, classes_attended, future_classes, future_attendance)
        plot.pyplot(plt)        

if __name__ == "__main__":
    main()

