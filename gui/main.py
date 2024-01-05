import asyncio
from controller.main import Controller

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  controller = Controller()
  loop.run_until_complete(controller.main())
