"""
ARGUS (Advanced Security Intelligence Platform)
Main CLI entry point for modular cybersecurity framework.
"""
import os
import sys
import argparse
import json
import logging
from core.ui import TerminalUI
from core.logging import ArgusLogger
from core.utils import ArgusUtils
from core.plugin_loader import PluginLoader
from core.animation import show_animation, show_loading_animation
from modules.network_scanner import NetworkScanner
from modules.port_scanner import PortScanner
from modules.breach_checker import BreachChecker
from modules.ssl_monitor import SSLMonitor
from modules.geoip_lookup import GeoIPLookup
from modules.threat_intel import ThreatIntel
from modules.audit_report import AuditReport

LOG_FILE = os.environ.get("ARGUS_LOG_FILE", "argus.log")
API_KEYS = {
    "geoip": os.environ.get("ARGUS_GEOIP_API_KEY"),
    "threat_intel": os.environ.get("ARGUS_THREAT_INTEL_API_KEY"),
    # Add more as needed
}

logger = ArgusLogger(LOG_FILE)
plugin_loader = PluginLoader("plugins")
plugin_loader.load_plugins()

MODULES = {
    "network-scan": NetworkScanner,
    "port-scan": PortScanner,
    "breach-check": BreachChecker,
    "ssl-monitor": SSLMonitor,
    "geoip": GeoIPLookup,
    "threat-intel": ThreatIntel,
    "audit-report": AuditReport,
}

def main():
    """
    Main entry point for ARGUS CLI.
    Parses arguments, validates input, runs selected module, and exports JSON report.
    """
    TerminalUI.print_header()
    parser = argparse.ArgumentParser(
        description="ARGUS: Advanced Security Intelligence Platform"
    )
    parser.add_argument("module", choices=MODULES.keys(), help="Module to run")
    parser.add_argument("--target", required=True, help="Target IP/hostname")
    parser.add_argument("--ports", help="Ports for port scan (comma-separated)")
    parser.add_argument("--output", help="Output JSON report file")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    if args.verbose:
        logger.set_level(logging.DEBUG)

    target_ip = ArgusUtils.resolve_hostname(args.target) if not ArgusUtils.validate_ip(args.target) else args.target
    if not target_ip:
        TerminalUI.print_error(f"Invalid target: {args.target}")
        logger.error(f"Invalid target: {args.target}")
        sys.exit(1)

    module_cls = MODULES.get(args.module)
    if not module_cls:
        TerminalUI.print_error(f"Unknown module: {args.module}")
        logger.error(f"Unknown module: {args.module}")
        sys.exit(1)

    try:
        module = module_cls(logger=logger, api_keys=API_KEYS)
        result = module.run(target_ip, ports=args.ports)
        TerminalUI.print_success(f"{args.module} completed successfully.")
        logger.success(f"{args.module} completed successfully.")
    except Exception as e:
        TerminalUI.print_error(f"Module error: {type(e).__name__}: {e}")
        logger.error(f"Module error: {type(e).__name__}: {e}")
        sys.exit(1)

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)
            TerminalUI.print_success(f"Report exported to {args.output}")
            logger.success(f"Report exported to {args.output}")
        except Exception as e:
            TerminalUI.print_error(f"Export error: {type(e).__name__}: {e}")
            logger.error(f"Export error: {type(e).__name__}: {e}")

def show_menu():
    """
    Displays interactive main menu for module selection.
    """
    TerminalUI.print_header()
    
    print("\n" + "="*70)
    print("AVAILABLE MODULES".center(70))
    print("="*70 + "\n")
    
    modules_list = [
        ("1", "network-scan", "Network Scanner", "Check host reachability (ping)"),
        ("2", "port-scan", "Port Scanner", "Scan open ports (threaded)"),
        ("3", "ssl-monitor", "SSL Monitor", "Check SSL/TLS certificates"),
        ("4", "geoip", "GeoIP Lookup", "Get geographic & ISP information"),
        ("5", "breach-check", "Breach Checker", "Check for known breaches"),
        ("6", "threat-intel", "Threat Intel", "Fetch threat intelligence data"),
        ("7", "audit-report", "Audit Report", "Generate security audit reports"),
        ("0", "exit", "Exit", "Exit ARGUS"),
    ]
    
    for num, cmd, name, desc in modules_list:
        print(f"  [{num}] {name:<20} - {desc}")
    
    print("\n" + "="*70)
    return modules_list

def interactive_menu():
    """
    Interactive menu-driven interface for ARGUS.
    """
    # Show startup animation on first load
    show_animation()
    
    while True:
        modules_list = show_menu()
        
        try:
            choice = input("\nSelect module [0-7]: ").strip()
            
            # Find selected module
            selected = None
            selected_cmd = None
            for num, cmd, name, desc in modules_list:
                if num == choice:
                    selected = name
                    selected_cmd = cmd
                    break
            
            if choice == "0" or selected == "Exit":
                TerminalUI.print_success("Thank you for using ARGUS. Goodbye!")
                sys.exit(0)
            
            if not selected:
                TerminalUI.print_error("Invalid selection. Please try again.")
                input("\nPress Enter to continue...")
                continue
            
            # Get target
            print(f"\nSelected: {selected}")
            print("="*70)
            target = input("Enter target IP or hostname: ").strip()
            
            if not target:
                TerminalUI.print_error("Target cannot be empty.")
                input("\nPress Enter to continue...")
                continue
            
            # Validate target
            target_ip = ArgusUtils.resolve_hostname(target) if not ArgusUtils.validate_ip(target) else target
            if not target_ip:
                TerminalUI.print_error(f"Invalid target: {target}")
                logger.error(f"Invalid target: {target}")
                input("\nPress Enter to continue...")
                continue
            
            # Get ports if needed
            ports = None
            if selected_cmd == "port-scan":
                ports_input = input("Enter ports (comma-separated, or leave blank for default): ").strip()
                if ports_input:
                    ports = ports_input
            
            # Get output file
            output_file = input("Enter output file (or leave blank for console only): ").strip() or None
            
            # Run module with loading animation
            print(f"\nRunning {selected} on {target_ip}...\n")
            show_loading_animation(f"Scanning {target_ip}")
            module_cls = MODULES.get(selected_cmd)
            
            try:
                module = module_cls(logger=logger, api_keys=API_KEYS)
                result = module.run(target_ip, ports=ports)
                TerminalUI.print_success(f"{selected_cmd} completed successfully.")
                logger.success(f"{selected_cmd} completed successfully.")
                
                # Display results
                print("\nRESULTS:")
                print("="*70)
                print(json.dumps(result, indent=2))
                print("="*70)
                
                # Export if requested
                if output_file:
                    try:
                        with open(output_file, "w", encoding="utf-8") as f:
                            json.dump(result, f, indent=2)
                        TerminalUI.print_success(f"Report exported to {output_file}")
                        logger.success(f"Report exported to {output_file}")
                    except Exception as e:
                        TerminalUI.print_error(f"Export error: {type(e).__name__}: {e}")
                        logger.error(f"Export error: {type(e).__name__}: {e}")
            
            except Exception as e:
                TerminalUI.print_error(f"Module error: {type(e).__name__}: {e}")
                logger.error(f"Module error: {type(e).__name__}: {e}")
            
            input("\nPress Enter to return to menu...")
        
        except KeyboardInterrupt:
            print("\n")
            TerminalUI.print_warning("Operation cancelled by user.")
            sys.exit(0)
        except Exception as e:
            TerminalUI.print_error(f"Error: {type(e).__name__}: {e}")
            input("\nPress Enter to continue...")

def main():
    """
    Main entry point for ARGUS CLI.
    Supports both interactive menu and command-line arguments.
    """
    # Check if command-line arguments provided
    if len(sys.argv) > 1:
        # Command-line mode
        parser = argparse.ArgumentParser(
            description="ARGUS: Advanced Security Intelligence Platform"
        )
        parser.add_argument("module", choices=MODULES.keys(), help="Module to run")
        parser.add_argument("--target", required=True, help="Target IP/hostname")
        parser.add_argument("--ports", help="Ports for port scan (comma-separated)")
        parser.add_argument("--output", help="Output JSON report file")
        parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
        args = parser.parse_args()

        if args.verbose:
            logger.set_level(logging.DEBUG)

        target_ip = ArgusUtils.resolve_hostname(args.target) if not ArgusUtils.validate_ip(args.target) else args.target
        if not target_ip:
            TerminalUI.print_error(f"Invalid target: {args.target}")
            logger.error(f"Invalid target: {args.target}")
            sys.exit(1)

        module_cls = MODULES.get(args.module)
        if not module_cls:
            TerminalUI.print_error(f"Unknown module: {args.module}")
            logger.error(f"Unknown module: {args.module}")
            sys.exit(1)

        try:
            module = module_cls(logger=logger, api_keys=API_KEYS)
            result = module.run(target_ip, ports=args.ports)
            TerminalUI.print_success(f"{args.module} completed successfully.")
            logger.success(f"{args.module} completed successfully.")
        except Exception as e:
            TerminalUI.print_error(f"Module error: {type(e).__name__}: {e}")
            logger.error(f"Module error: {type(e).__name__}: {e}")
            sys.exit(1)

        if args.output:
            try:
                with open(args.output, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2)
                TerminalUI.print_success(f"Report exported to {args.output}")
                logger.success(f"Report exported to {args.output}")
            except Exception as e:
                TerminalUI.print_error(f"Export error: {type(e).__name__}: {e}")
                logger.error(f"Export error: {type(e).__name__}: {e}")
    else:
        # Interactive menu mode
        interactive_menu()

if __name__ == "__main__":
    main()
