import os
import shutil
import logging

def log_setup(dest):
    # Setup logging
    log_file = os.path.join(dest, 'file_organizer_log.txt')
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.info('Logging started')
    

def banner():
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Welcome message
    print("""
    *****************************
    *   File Organizer v1.0.0   *
    *   By: Thushara Thiwanka   *
    *****************************
""")


def main():
    # Welcome banner
    banner()

    # Get the directory to work in
    print("--| Example: C:\\Users\\Thushara\\Downloads |--\n")
    src = input('Enter directory to work in: ')

    # Get the directory to move the files to
    dest = input('Enter directory to move files to: ')

    # Setup logging
    log_setup(dest)

    # Make sure the directory exists
    if not os.path.isdir(src):
        print('Error: {} is not a directory'.format(src))
        return
    if not os.path.isdir(dest):
        print('Error: {} is not a directory'.format(dest))
        return

    # Get the files in the directory without folders and ignore log.txt
    files = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f)) and f != 'file_organizer_log.txt']

    # Loop through the files
    for file in files:

        # Get the file extension
        ext = os.path.splitext(file)[1]

        # Create the subdirectory with capitalized extension name
        new_dir = os.path.join(dest, ext[1:].upper())

        # Create the subdirectory if it doesn't exist
        if not os.path.isdir(new_dir):
            os.mkdir(new_dir)

        # Check if the file exists in the subdirectory before moving
        new_file = os.path.join(new_dir, file)
        if os.path.isfile(new_file):

            logging.error('Error: {} already exists in {}'.format(file, new_dir))

            # Move duplicate files to a duplicate folder
            dup_dir = os.path.join(dest, 'Duplicates')
            if not os.path.isdir(dup_dir):
                os.mkdir(dup_dir)
            dup_file = os.path.join(dup_dir, file)
            shutil.move(os.path.join(src, file), dup_file)
            
            logging.info('Moved duplicate file to {}'.format(dup_file))

            continue

        # Move the file
        shutil.move(os.path.join(src, file), new_file)
        
        logging.info("Moving: '{}' to '{}'".format(os.path.basename(file), ext[1:].upper()))

    print("\nDone - Check the 'file_organizer_log.txt' file for more details\n")
    print("Happy Organizing! :) \n")
    logging.info('logging finished')
    
    # close the log file
    logging.shutdown()

    # Prevent the program from exiting
    input('Press Enter to exit')

if __name__ == '__main__':
    main()
