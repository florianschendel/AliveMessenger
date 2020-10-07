import AliveMessengerUUID
import AliveMessengerHelper
import asyncio
import sys
import time
from bleak import discover
from bleak import BleakClient

async def discovery():
    devices = await discover()
    address = []
    name = []
    for d in devices:
        device_name = d.name
        device_address = d.address
        if device_name.startswith('Alive') == True:
            address.append(d.address)
            name.append(d.name)
    i = 0
    print ("##################################################################################################")
    for a in address:
        print("Device entry:",i,"Device Name:",name[i],"Device address:",address[i])
        i += 1

    while True:
        try:
            print ("##################################################################################################")
            device_selection = int(input("Please select the device entry number: "))
            print ("\n")
            ble_address = address[device_selection]
            break
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Please use only the device entry numbers")
        except IndexError:
            print("Device entry number not exists")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    async with BleakClient(ble_address, loop=loop) as client:
        while True:
            try:
                print("\n" + "Please select the action: ")
                print("Type in 0 for Device Information")
                print("Type in 1 to get tracking information")
                print("Type in 2 to check messages")
                print("Type in 3 to send a message")
                print("Type in 4 to get Location data")
                print("Type in 9 to terminate the program")
                action_selection = int(input("Please select the device entry number: "))

                if action_selection == 0:
                    # Check System information
                    battery_status = await client.read_gatt_char(AliveMessengerUUID.BT_LVL_UUID)
                    vendor = await client.read_gatt_char(AliveMessengerUUID.MANUF_UUID)
                    model = await client.read_gatt_char(AliveMessengerUUID.MODEL_UUID)
                    hardware_rev = await client.read_gatt_char(AliveMessengerUUID.HW_REV_UUID)
                    firmware_rev = await client.read_gatt_char(AliveMessengerUUID.FW_REV_UUID)
                    serial_number = await client.read_gatt_char(AliveMessengerUUID.SERIAL_UUID)
                    # Report Basic device information
                    print ("##################################################################################################")
                    print ("###################################### Device Information ########################################")
                    print ("##################################################################################################")
                    print ("Hersteller:",vendor.decode('utf-8'))
                    print ("Model/Typ:",model.decode('utf-8'))
                    print ("Hardware Revision:",hardware_rev.decode('utf-8'))
                    print ("Firmware:",firmware_rev.decode('utf-8'))
                    print ("Serial Number:",serial_number.decode('utf-8'))
                    print ("Battery status:",int.from_bytes(battery_status, byteorder='little'),"%")

                elif action_selection == 1:
                    # Check Tracking
                    TRK_GSM_STD_ITVL = await client.read_gatt_char(AliveMessengerUUID.TRK_GSM_STD_ITVL_UUID)
                    TRK_IRM_STD_ITVL = await client.read_gatt_char(AliveMessengerUUID.TRK_IRM_STD_ITVL_UUID)
                    TRK_GSM_EVT_ITVL = await client.read_gatt_char(AliveMessengerUUID.TRK_GSM_EVT_ITVL_UUID)
                    TRK_IRM_EVT_ITVL = await client.read_gatt_char(AliveMessengerUUID.TRK_IRM_EVT_ITVL_UUID)
                    TRK_GSM_CTM_ITVL = await client.read_gatt_char(AliveMessengerUUID.TRK_GSM_CTM_ITVL_UUID)
                    TRK_IRM_CTM_ITVL = await client.read_gatt_char(AliveMessengerUUID.TRK_IRM_CTM_ITVL_UUID)
                    trackingMode = await client.read_gatt_char(AliveMessengerUUID.TRK_MODE_UUID)
                    # Compare Tracking mode
                    print ("##################################################################################################")
                    print ("###################################### Tracking information ######################################")
                    print ("##################################################################################################")
                    if trackingMode[0] == AliveMessengerUUID.TRK_MODE_DISABLE:
                        print ("Tracking Mode: " + "Disabled")
                    elif trackingMode[0] == AliveMessengerUUID.TRK_MODE_STANDARD:
                        print ("Tracking Mode: " + "Standard")
                        print ("Tracking Interval GSM Standard mode:",int.from_bytes(TRK_GSM_STD_ITVL, byteorder='little'), "sec")
                        print ("Tracking Interval Iridium Standard mode:",int.from_bytes(TRK_IRM_STD_ITVL, byteorder='little'), "sec")
                    elif trackingMode[0] == AliveMessengerUUID.TRK_MODE_REALTIME:
                        print ("Tracking Mode: " + "Event/Realtime")
                        print ("Tracking Interval GSM Event mode: ",int.from_bytes(TRK_GSM_EVT_ITVL, byteorder='little'), "sec")
                        print ("Tracking Interval Iridium Event mode: ",int.from_bytes(TRK_IRM_EVT_ITVL, byteorder='little'), "sec")
                    elif trackingMode[0] == AliveMessengerUUID.TRK_MODE_CUSTOM :
                        print ("Tracking Mode: " + "Custom")
                        print ("Tracking Interval GSM Custom mode: ",int.from_bytes(TRK_GSM_CTM_ITVL, byteorder='little'), "sec")
                        print ("Tracking Interval Iridium Custom mode: ",int.from_bytes(TRK_IRM_CTM_ITVL, byteorder='little'), "sec")
                    elif trackingMode[0] == AliveMessengerUUID.TRK_MODE_SOS:
                        print ("Tracking Mode: " + "SOS")
                    else:
                        print ("Tracking Mode: " + "Unknown")

                elif action_selection == 2:
                    # Check messages
                    currentSender = await client.read_gatt_char(AliveMessengerUUID.MSG_ADDR_UUID)
                    currentMessage = await client.read_gatt_char(AliveMessengerUUID.MSG_DATA_UUID)
                    # Print received message
                    print ("##################################################################################################")
                    print ("######################################## Received messages #######################################")
                    print ("##################################################################################################")
                    print ("Sender: ",str(currentSender, 'utf-8'))
                    print ("Message: ",str(currentMessage, 'utf-8'))

                elif action_selection == 3:
                    print ("##################################################################################################")
                    print ("######################################## Send messages #######################################")
                    print ("##################################################################################################")
                    # Send a message
                    # Receiver
                    email_Phone = str(input("E-Mail or phone number: "))
                    receiverAddress = bytearray(email_Phone, 'utf-8')
                    # Message itself
                    message = str(input("Enter your message: "))
                    outMessage = bytearray(message,'utf-8')
                    # Check before delivery
                    print("Do you want to send this message?")
                    print("Receiver: ",email_Phone)
                    print("Message: ",message)
                    send = str(input("y/n: "))
                    if send == "y":
                        await client.write_gatt_char(AliveMessengerUUID.MSG_ADDR_UUID, receiverAddress, response=True)
                        await client.write_gatt_char(AliveMessengerUUID.MSG_DATA_UUID, outMessage, response=True)
                        status = int.from_bytes(await client.read_gatt_char(AliveMessengerUUID.MSG_OUT_STATUS_UUID), byteorder='little')
                        print("Waiting for Delivery (Timeout 3 minutes)")
                        timeout = 10
                        retries = 0
                        retry_max = 18
                        while status != 3:
                            time.sleep(timeout)
                            status = int.from_bytes(await client.read_gatt_char(AliveMessengerUUID.MSG_OUT_STATUS_UUID), byteorder='little')
                            retries = retries + 1
                            if retries >= retry_max:
                                print("Timeout, Message delivery delayed")
                                break

                elif action_selection == 4:
                    loc_ftrs = await client.read_gatt_char(AliveMessengerUUID.LOC_FTRS_UUID)
                    loc_qlty = await client.read_gatt_char(AliveMessengerUUID.LOC_QLTY_UUID)
                    loc_data = await client.read_gatt_char(AliveMessengerUUID.LOC_DATA_UUID)

                    data_string_flags = AliveMessengerHelper.BitMerge(loc_data,AliveMessengerUUID.LOC_DATA_BYTE_FLAGS)
                    feature_flags = AliveMessengerHelper.BitMerge(loc_ftrs,AliveMessengerUUID.LOC_FTRS_BYTES)
                    # Print output only for debugging
                    #print ("Data Bit Flags:",str(format(data_string_flags,'#010b')))
                    #print ("Features Bit Flags:",str(format(feature_flags,'#010b')))
                    print ("Location Quality: " + "NbSat:",loc_qlty[AliveMessengerUUID.LOC_QLTY_BYTE_NBSAT[0]],"HDOP:",loc_qlty[AliveMessengerUUID.LOC_QLTY_BYTE_HDOP[0]])

                    elevation = AliveMessengerHelper.BitMerge(loc_data,AliveMessengerUUID.LOC_DATA_BYTE_ELEVATION)
                    heading = AliveMessengerHelper.BitMerge(loc_data,AliveMessengerUUID.LOC_DATA_BYTE_HEADING)
                    speed = AliveMessengerHelper.BitMerge(loc_data,AliveMessengerUUID.LOC_DATA_BYTE_SPEED)
                    latitude = AliveMessengerHelper.BitMerge(loc_data,AliveMessengerUUID.LOC_DATA_BYTE_LATITUDE)
                    longitude = AliveMessengerHelper.BitMerge(loc_data,AliveMessengerUUID.LOC_DATA_BYTE_LONGITUDE)
                    year = AliveMessengerHelper.DateTime(loc_data,AliveMessengerUUID.LOC_DATA_BYTE_YEAR)
                    month = AliveMessengerHelper.DateTime(loc_data,AliveMessengerUUID.LOC_DATA_BYTE_MONTH)
                    day = AliveMessengerHelper.DateTime(loc_data,AliveMessengerUUID.LOC_DATA_BYTE_DAY_OF_MONTH)
                    hours = AliveMessengerHelper.DateTime(loc_data,AliveMessengerUUID.LOC_DATA_BYTE_HOURS)
                    minutes = AliveMessengerHelper.DateTime(loc_data,AliveMessengerUUID.LOC_DATA_BYTE_MINUTES)
                    seconds = AliveMessengerHelper.DateTime(loc_data,AliveMessengerUUID.LOC_DATA_BYTE_SECONDS)
                    print("Höhe:",elevation,"Meter")
                    print("Heading:",heading,"Grad")
                    print("Speed:",speed,"kmh")
                    print("Latitude:",latitude/10000000)
                    print("Longitude:",longitude/10000000)
                    print("Date:",str('%04d' % year) + str('%02d' % month) + str('%02d' % day),"Time:",str('%02d' % hours) + ":" + str('%02d' % minutes) + ":" + str('%02d' % seconds),"UTC")
                    #print('%02d' % n)

                elif action_selection == 9:
                    break
            except OSError as err:
                print("OS error: {0}".format(err))
            except ValueError as errorvalue:
                print("Please use only the device entry numbers")
                print("Value Error: {0}".format(errorvalue))
            except IndexError as errorindex:
                print("Device entry number not exists")
                print("Index Error: {0}".format(errorindex))
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise

loop = asyncio.get_event_loop()
loop.run_until_complete(discovery())
