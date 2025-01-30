# Biotic 3D Printer - README

## Overview
The Biotic 3D Printer is an open-source syringe-based extrusion system designed to print natural biotic materials such as pectin, chitosan, and cellulose. Unlike traditional FDM printers that rely on thermoplastics, this printer deposits viscous biocomposites that dry over time. This project aims to enable accessible research and development in sustainable, bio-based manufacturing.

## Repository Organization
This repository is structured as follows:

### 1. **CAD/**
   - Contains the full printer assembly files in Fusion 360 format.
   - Includes individual component models and assemblies.

### 2. **BOM/**
   - Excel spreadsheet listing all required components.
   - Includes part numbers, sources, quantities, and estimated costs.

### 3. **Slicer Profile/**
   - PrusaSlicer profile tailored for the Biotic 3D Printer.
   - Post-processing script (if applicable) for generating G-code compatible with RepRapFirmware.

### 4. **RepRap Config/**
   - `config.zip`: Contains all necessary configuration files for RepRapFirmware on the Duet 3 6HC.
   - `macros.zip`: Collection of macros for printer setup, calibration, and operation.

## Getting Started
1. **Hardware Setup:**
   - Assemble the printer according to the CAD files.
   - Ensure all mechanical components are properly installed and secured.

2. **Electronics & Firmware:**
   - Flash the Duet 3 6HC with RepRapFirmware.
   - Extract the contents of `RepRap Config/config.zip` onto the Duet SD card.
   - Load macros from `macros.zip` for easy calibration and operation.

3. **Slicing & Printing:**
   - Install PrusaSlicer and import the provided profile.
   - Adjust slicing settings based on the material being printed.
   - Generate G-code and upload it to the Duet Web Control interface.

## Notes
- This project is a work in progress, and future updates will enhance printer autonomy and material compatibility.
- Contributions and improvements from the community are welcome!

## License
This project is released under an open-source license to encourage collaboration and innovation.

For any questions or contributions, feel free to reach out or submit an issue/request.

