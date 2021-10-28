from pynrfjprog import HighLevel
from pynrfjprog.APIError import *



api = HighLevel.API()

def get_probe_snrs(api):
    with HighLevel.API() as api:
        serials = api.get_connected_probes()
        return(serials)
    #serialsnums = HighLevel.API().get_connected_probes()   figure out what other function calls would be needed to make this work
    #return (serialsnums)



def flash_mcu(snr):

    

    program_options = HighLevel.ProgramOptions(
                erase_action=HighLevel.EraseAction.ERASE_ALL,
                reset = HighLevel.ResetAction.RESET_SYSTEM,
                verify = HighLevel.VerifyAction.VERIFY_READ
            )

    with HighLevel.API() as api:
    
    
        with HighLevel.DebugProbe(api,snr) as probe:
            result = probe.program(r'C:\Users\garre\Trackonomy\Desktop\Onyx Test programming\Modem_Power_ON_Firmware.hex',program_options = program_options)
            print(result)
            if result == NrfjprogdllErr.SUCCESS:
                print("test")
            probe.verify(r'C:\Users\garre\Trackonomy\Desktop\Onyx Test programming\Modem_Power_ON_Firmware.hex')






def Update_modem(snr):

    
    api = HighLevel.API()
    api.open()
    probe = HighLevel.IPCDFUProbe(api, snr, HighLevel.CoProcessor.CP_MODEM)
    probe.program("mfw_nrf9160_1.3.1.zip")
    probe.verify("mfw_nrf9160_1.3.1.zip")
    print("Modem Sucsessfully updated")
    api.close()


if __name__ == "__main__":
    serial = get_probe_snrs(api)
    print(serial)

