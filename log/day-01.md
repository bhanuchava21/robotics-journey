# Day 1 (Nov 18, 2026)

**Setup:** UTM VM on MacBook M3 Pro → Ubuntu 24.04 ARM64 → ROS 2 Jazzy

## What I did
- Ran talker/listener demo: C++ publisher → Python subscriber on `/chatter`
- Drove turtlesim with the keyboard; arrow keys publish to `/turtle1/cmd_vel`

## What broke and how I fixed it
- Deleted the installer ISO before removing it from UTM → QEMU "No such file" error. Fixed by deleting the USB/CD drive in the VM settings.
- Blurry display → installed `spice-vdagent` and set the resolution in Ubuntu.

## Learned
ROS 2 nodes communicate via topics (publish/subscribe), much like pub/sub in backend systems.
