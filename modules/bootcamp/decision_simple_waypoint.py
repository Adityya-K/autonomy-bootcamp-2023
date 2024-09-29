"""
BOOTCAMPERS TO COMPLETE.

Travel to designated waypoint.
"""

from .. import commands
from .. import drone_report

# Disable for bootcamp use
# pylint: disable-next=unused-import
from .. import drone_status
from .. import location
from ..private.decision import base_decision


# Disable for bootcamp use
# No enable
# pylint: disable=duplicate-code,unused-argument


class DecisionSimpleWaypoint(base_decision.BaseDecision):
    """
    Travel to the designed waypoint.
    """

    def __init__(self, waypoint: location.Location, acceptance_radius: float) -> None:
        """
        Initialize all persistent variables here with self.
        """
        self.waypoint = waypoint
        print(f"Waypoint: {waypoint}")

        self.acceptance_radius = acceptance_radius

        # ============
        # ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
        # ============

        self.land_command_issued = False

        # ============
        # ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
        # ============

    def run(
        self,
        report: drone_report.DroneReport,
        landing_pad_locations: "list[location.Location]",
    ) -> commands.Command:
        """
        Make the drone fly to the waypoint.

        You are allowed to create as many helper methods as you want,
        as long as you do not change the __init__() and run() signatures.

        This method will be called in an infinite loop, something like this:

        ```py
        while True:
            report, landing_pad_locations = get_input()
            command = Decision.run(report, landing_pad_locations)
            put_output(command)
        ```
        """
        # Default command
        command = commands.Command.create_null_command()

        # ============
        # ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
        # ============

        to_waypoint_x = self.waypoint.location_x - report.position.location_x
        to_waypoint_y = self.waypoint.location_y - report.position.location_y
        if (
            report.status == drone_status.DroneStatus.HALTED
            and not report.status == drone_status.DroneStatus.LANDED
        ):
            if (
                abs(to_waypoint_x) <= self.acceptance_radius
                and abs(to_waypoint_y) <= self.acceptance_radius
            ):
                command = commands.Command.create_land_command()
            else:
                command = commands.Command.create_set_relative_destination_command(
                    to_waypoint_x, to_waypoint_y
                )
        elif report.status == drone_status.DroneStatus.MOVING:
            if (
                abs(to_waypoint_x) <= self.acceptance_radius
                and abs(to_waypoint_y) <= self.acceptance_radius
            ):
                command = commands.Command.create_land_command()

        # ============
        # ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
        # ============

        return command
