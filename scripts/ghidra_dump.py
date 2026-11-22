# Ghidra postscript. Run with analyzeHeadless and -postScript.
# Environment: BERIL_GHIDRA_OUT points to the JSON output path.
import json
import os

from ghidra.program.model.symbol import SymbolType

OUT = os.environ.get("BERIL_GHIDRA_OUT", "/tmp/beril-ghidra.json")
SUSPICIOUS = {"strcpy", "strcat", "sprintf", "gets", "memcpy", "system", "popen",
              "execve", "CreateProcessA", "WinExec", "recv", "read", "VirtualProtect"}

data = {"program": currentProgram.getName(), "functions": [], "imports": [], "strings": [], "suspicious": []}

fm = currentProgram.getFunctionManager()
count = 0
for f in fm.getFunctions(True):
    data["functions"].append({"name": f.getName(), "entry": str(f.getEntryPoint()),
                              "size": f.getBody().getNumAddresses()})
    count += 1
    if count >= 20000:
        break

for sym in currentProgram.getSymbolTable().getAllSymbols(True):
    if sym.getSymbolType() != SymbolType.FUNCTION:
        continue
    name = sym.getName()
    refs = getReferencesTo(sym.getAddress())
    for ref in refs:
        data["imports"].append({"name": name, "from": str(ref.getFromAddress())})
    if name.split(".")[-1] in SUSPICIOUS:
        data["suspicious"].append(name)
        for ref in refs:
            data["suspicious"].append("%s <- %s" % (name, ref.getFromAddress()))

listing = currentProgram.getListing()
count = 0
for d in listing.getDefinedData(True):
    value = d.getValue()
    if isinstance(value, str) and len(value) > 3:
        data["strings"].append({"address": str(d.getAddress()), "value": value[:200]})
        count += 1
        if count >= 5000:
            break

with open(OUT, "w") as fh:
    json.dump(data, fh, indent=2)
print("beril: wrote %s" % OUT)
