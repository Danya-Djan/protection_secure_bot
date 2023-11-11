import asyncio
import logging
from wrapper import run_bot

#------------------------------------------------------------------------------
# Created by DanyaDjan and Arscool
#------------------------------------------------------------------------------

def main():
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        print("Interrupted by user, shutting down")
        return

if __name__ == "__main__":
    # if not is_updated:
    #     rewrite_csv()
    #     is_updated = True
    #     print("Database updated")
    main()

