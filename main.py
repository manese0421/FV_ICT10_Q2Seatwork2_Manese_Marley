from js import document
from pyscript import display

def general_weighted_average(event=None):
    # it first clears any previous outputs before showing any new ones
    document.getElementById("student_info").innerText = ""
    document.getElementById("summary").innerText = ""
    document.getElementById("output").innerText = ""

    # document.getElementById("id_name").value reads what the user entered in the box
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    
    # we need to make sure that the box is NOT empty before this runs
    try:
        # when the user enters a number, it is read as text
        # we need to convert it to a float so we can use it to calculate
        science = float(document.getElementById("science").value)
        math = float(document.getElementById("math").value)
        english = float(document.getElementById("english").value)
        filipino = float(document.getElementById("filipino").value)
        ict = float(document.getElementById("ict").value)
        pe = float(document.getElementById("pe").value)
    except ValueError:
        # if any box is empty/invalid, this runs instead of the code crashing
        display("⚠️ Please enter a valid number for all grades.", target="output")
        return  # in this case, the function stops here

    # 'subjects' is a list and it stores the names of each subject
    # 'units' is a tuple and it stores the corresponding unit weight for each subject
    subjects = ["Science", "Math", "English", "Filipino", "ICT", "PE"]
    units = (5, 5, 5, 3, 2, 1)
    # if the number is higher, it has a higher effect in the final GWA

    # we then multiply each grade by its unit weight and all of them together to get the weighted sum
    weighted_sum = (science*5 + math*5 + english*5 + filipino*3 + ict*2 + pe*1)

    # sum() adds up all the numbers in 'units'
    total_units = sum(units)

    # we divide the weighted sum by the amount of units to get the GWA
    gwa = weighted_sum / total_units


    # use f-strings to turn the variable values into text to display on the page
    display(f"Name: {first_name} {last_name}", target="student_info")

    summary = f"""
    Science: {science:.0f}<br>
    Math: {math:.0f}<br>
    English: {english:.0f}<br>
    Filipino: {filipino:.0f}<br>
    ICT: {ict:.0f}<br>
    PE: {pe:.0f}
    """

    # display subject and grade summary under the 'summary' section of the html
    display(summary, target="summary")

    # shows the calculated GWA with 2 decimal places (.2f --> 2 digits after the decimal)
    display(f"Your General Weighted Average is: <b>{gwa:.2f}</b>", target="output")
