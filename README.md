# MCAT_ModularCodingAnalysisTool

## Philosphy

APIs from unmanaged software or hardware can change without warning. A good example of this would be moving from one target hardware to another. To get around this, calls to APIs that can change (we call these unstable interfaces) should be abstracted with an interposing layer. This interposer provides a stable interface for high level programming, and can translate that stable interface to many targets. An unstable interface called by the interposer is called an Abstracted Software Module (ASM) and software or code that calls the interposer is called Calling Software Module (CSM)

## Benefits
1. If an unstable interface changes, only the interposer needs updating. This is typically a much simpler (and therefore less risky) job than updating high level software integrated directly into these unstable interfaces.
2. By swapping out interposers at compile/run time, you can support many different architectures/OSs at the same time with the same CSM.
3. Tests on high level software are carried out via the stable interface provided by the interposer, thus changes to unstable interfaces do not require changes to tests of CSMs.
4. Tests on the interposer remain static also, as the api to the CSM is static. Strong testing of this interface ensures compatbility between changing ASMs and old CSMs.

## Design Intent
The idea of this software is to provider a linter to enforce these coding practices.

Any function calls from new code where the function being called’s api could change (unstable interface), for example code considered hardware specific (i.e could change with hardware) or where the interface to an externally developed api, is in one folder (or listed in a file). Functions defined in the folder are added to the ASM catalog (ASMC). The linter scans code, if the new code has a call to another function that’s not already in the ASMC, it prompts the user whether they consider this a call to an unstable interface or not i.e should this call be abstracted behind an interposer.

## Status

Work in progress.