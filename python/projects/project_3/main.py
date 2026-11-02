import csv

# ============================================================
# BLOCK 01: FILE ACCESS AND CSV READING
# ============================================================

try:
    # Open the CSV file in read mode.
    # The 'with' statement automatically closes the file when
    # execution leaves this block.
    with open("data/machine_log.csv", "r") as file:
        print("\nFile opened successfully\n")

        # DictReader reads each CSV row as a dictionary.
        # CSV column headers become dictionary keys.
        reader = csv.DictReader(file)

        # ====================================================
        # BLOCK 02: INITIALIZE DATA STRUCTURES AND COUNTERS
        # ====================================================

        # Stores the total number of records for each severity.
        Severity_count = {"INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}

        # Stores the number of errors recorded by each machine.
        Error_Count_By_Machine = {}

        # Stores the occurrence count of each unique error message.
        Error_Message_Count = {}

        # Tracks the total number of CSV records processed.
        total_records_processed = 0

        # ====================================================
        # BLOCK 03: LOAD RECORDS AND CHECK FOR EMPTY FILES
        # ====================================================

        # Convert the CSV reader into a list.
        # This allows us to check whether records exist before
        # starting the analysis.
        rows = list(reader)

        if len(rows) == 0:
            print("\n---- No records found in the CSV file ----\n")

        else:
            # ====================================================
            # BLOCK 04: EXTRACT AND PROCESS CSV RECORDS
            # ====================================================

            print("\n---- ALL LOGS ----\n")

            # Process each CSV record individually.
            for row in rows:
                # Increment the total record counter.
                total_records_processed += 1

                # Extract individual values using CSV column names.
                Machine_Id = row["machine_id"]
                Severity = row["severity"]
                Message = row["message"]
                Timestamp = row["timestamp"]

                # ====================================================
                # BLOCK 05: UPDATE SEVERITY STATISTICS
                # ====================================================

                # Increment the counter for the current severity.
                Severity_count[Severity] += 1

                # ====================================================
                # BLOCK 06: COUNT ERRORS BY MACHINE AND MESSAGE
                # ====================================================

                # Create a machine entry if it does not exist.
                # This also allows machines with zero errors to be tracked.
                if Machine_Id not in Error_Count_By_Machine:
                    Error_Count_By_Machine[Machine_Id] = 0

                # Only ERROR records contribute to error statistics.
                if Severity == "ERROR":
                    # Increment the error count for this machine.
                    Error_Count_By_Machine[Machine_Id] += 1

                    # Create a message entry if it is encountered
                    # for the first time.
                    if Message not in Error_Message_Count:
                        Error_Message_Count[Message] = 0

                    # Increment the occurrence count of this message.
                    Error_Message_Count[Message] += 1

                # ====================================================
                # BLOCK 07: DISPLAY INDIVIDUAL LOG RECORDS
                # ====================================================

                # Display each record in a consistently aligned format.
                print(f"{Machine_Id:<8} | {Severity:<8} | {Message:<35} | {Timestamp}")

                print("-" * 82)

            # ====================================================
            # BLOCK 08: GENERATE GENERAL AND SEVERITY REPORTS
            # ====================================================

            # Display the total number of processed records.
            print("\n---- TOTAL ROWS PROCESSED ----\n")
            print(f"Simulated Data: {total_records_processed}")
            print("\n----------------------")

            # Display the count of each severity level.
            print("\n---- SEVERITY SUMMARY ----\n")

            for severity, count in Severity_count.items():
                print(severity, ":", count)

            print("\n----------------------")

            # ====================================================
            # BLOCK 09: GENERATE MACHINE AND ERROR MESSAGE REPORTS
            # ====================================================

            # Display the total errors recorded for each machine.
            print("\n---- ERROR REPORT BY MACHINE ----\n")

            if Error_Count_By_Machine:
                for machine_id, count in Error_Count_By_Machine.items():
                    print(machine_id, ":", count)
            else:
                print("[ No machine records found ]")

            print("\n----------------------")

            # Display how frequently each unique error message occurred.
            print("\n---- ERROR MESSAGE OCCURRENCES ----\n")

            if Error_Message_Count:
                for Message, count in Error_Message_Count.items():
                    print(Message, ":", count)
            else:
                print("[ No error messages recorded in this file ]")

            print("\n----------------------")

            # ====================================================
            # BLOCK 10: IDENTIFY THE MOST ERROR-PRONE MACHINE
            # ====================================================

            # Check whether at least one machine has recorded an error.
            if any(Error_Count_By_Machine.values()):
                # Find the machine with the highest error count.
                Most_Error_Machine = max(
                    Error_Count_By_Machine, key=Error_Count_By_Machine.get
                )

                print("\n---- MOST ERROR-PRONE MACHINE ----\n")
                print(f"Machine: {Most_Error_Machine}")
                print(f"Total Errors: {Error_Count_By_Machine[Most_Error_Machine]}")

            else:
                print("\n---- MOST ERROR-PRONE MACHINE ----\n")
                print("[ No errors recorded across any machine. ]")

            print("\n----------------------")


# ============================================================
# ERROR HANDLING: MISSING INPUT FILE
# ============================================================

except FileNotFoundError:
    print("Error: File Not Found!")