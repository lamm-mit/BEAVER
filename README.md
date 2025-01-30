# BEAVER: An Open-Source and Low-Cost Dual Extruder 3D Printer for Macroscale Biotic Materials 

We report the design and fabrication of a novel, dual-extruder biotic 3D printer tailored for precise deposition of natural biomaterials such as pectin, chitosan, and cellulose. Moving beyond the limitations of traditional thermoplastic extrusion, this printer utilizes a syringe-based mechanical extruder to deposit viscous biotic material hydrogels. The integration of a dual-extruder system enables the creation of multi-material prints and complex geometries, offering new possibilities for sustainable and bio-inspired manufacturing. Designed with accessibility and versatility in mind, the system features user-friendly operation suitable for non-experts, open-source hardware and software, and compatibility with a wide range of biomaterials. This platform addresses existing challenges in biomaterial 3D printing, such as limited material diversity and geometric complexity, while supporting diverse applications in biomaterials research and sustainable design. By providing a robust, customizable, and open-source platform, this work aims to empower researchers, educators, and innovators to advance biomaterials research and expand the reach of sustainable additive manufacturing. The printer fosters a collaborative community and lays the groundwork for further exploration of bio-inspired designs and materials. 

## Overview
BEAVER is an open-source syringe-based dual-extruder FDM 3D Printer that uses natural biotic material feedstock such as pectin, chitosan, and cellulose. Unlike traditional FDM printers that rely on thermoplastics, this printer deposits viscous biocomposites that dry over time. This project aims to enable accessible research and development in sustainable, bio-based manufacturing.

![Printer Render](Media/Final_Render.png)

## Repository Organization
This repository is structured as follows:

### 1. **CAD/**
   - Contains the full printer assembly files in Autodesk Fusion format.
   - Includes individual component models and assemblies.

### 2. **BOM/**
   - Excel spreadsheet listing all required components.
   - Includes part, quantities, and linked sources.

### 3. **Slicer Profile/**
   - PrusaSlicer profile tailored for BEAVER.
   - Post-processing script for altering sliced files for dual-extruder printing.

### 4. **RepRap Config/**
   - `config.zip`: Contains all necessary configuration files for RepRapFirmware on the Duet 3 6HC.
   - `macros.zip`: Collection of macros for printer calibration and workflow.

## Getting Started
1. **Hardware Setup:**
   - Assemble the printer according to the CAD files.
   - Ensure all mechanical components are properly installed and secured.
   - The frame is assembled used blind joints.

2. **Electronics & Firmware:**
   - Set up the Duet 3 Main Board 6HC in SBC mode with the Raspberry Pi and Duet 3 Expansion Board 3HC according to the Duet start up guide.
   - Extract the contents of `RepRap Config/config.zip` and upload them in the Duet Web Control page.
   - Load macros from `macros.zip` for Z-offset calibration and operation.

3. **Slicing & Printing:**
   - Install PrusaSlicer and import the provided profile.
   - Adjust slicing settings based on the material being printed.
   - Generate G-code and upload it to the Duet Web Control interface.
   - For dual material printer, upload the post-processor according to PrusaSlicer instructions.

## Notes
- This project fully functioning, any future updates will continue to be upload here.
- Contributions and improvements from the community are welcome!

## License
This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivs (CC BY-NC-ND) license. This means you are free to share the material with proper attribution, but you may not use it for commercial purposes or create derivative works.

## Citation

Please cite this work as follows:

```bibtex
@article{BEAVERdeAlvaBuehler2025,
      title={An Open-Source and Low-Cost Dual Extruder 3D Printer for Macroscale Biotic Materials}, 
      author={Jesse P. de Alva and Markus J. Buehler},
      year={2025},
      eprint={xxx.yyyyy},
      archivePrefix={},
      primaryClass={},
      url={}, 
}```
