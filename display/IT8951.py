import RPi.GPIO as GPIO
import spidev

class IT8951():
    # built in I80 command code
    IT8951_TCON_SYS_RUN = 0x0001
    IT8951_TCON_STANDBY = 0x0002
    IT8951_TCON_SLEEP = 0x0003
    IT8951_TCON_REG_RD = 0x0010
    IT8951_TCON_REG_WR = 0x0011
    IT8951_TCON_MEM_BST_RD_T = 0x0012
    IT8951_TCON_MEM_BST_RD_S = 0x0013
    IT8951_TCON_MEM_BST_WR = 0x0014
    IT8951_TCON_MEM_BST_END = 0x0015
    IT8951_TCON_LD_IMG = 0x0020
    IT8951_TCON_LD_IMG_AREA = 0x0021
    IT8951_TCON_LD_IMG_END = 0x0022

    # I80 user defined command
    USDEF_I80_CMD_DPY_AREA = 0x0034
    USDEF_I80_CMD_GET_DEV_INFO = 0x0302
    USDEF_I80_CMD_DPY_BUF_AREA = 0x0037
    USDEF_I80_CMD_VCOM = 0x0039

    # panel size
    IT8951_PANEL_WIDTH = 1024
    IT8951_PANEL_HEIGHT = 758

    # rotate mode
    IT8951_ROTATE_0 = 0
    IT8951_ROTATE_90 = 1
    IT8951_ROTATE_180 = 2
    IT8951_ROTATE_270 = 3

    # pixel mode : BPP: bit per pixel
    IT8951_2BPP = 0
    IT8951_3BPP = 1
    IT8951_4BPP = 2
    IT8951_8BPP = 3

    # waveform mode
    IT8951_MODE_0 = 0
    IT8951_MODE_1 = 1
    IT8951_MODE_2 = 2
    IT8951_MODE_3 = 3
    IT8951_MODE_4 = 4

    # endian type
    IT8951_LDIMG_L_ENDIAN = 0
    IT8951_LDIMG_B_ENDIAN = 1

    # auto LUT
    IT8951_DIS_AUTO_LUT = 0
    IT8951_EN_AUTO_LUT = 1

    # LUT engine status
    IT8951_ALL_LUTE_BUSY = 0xFFFF

    # display base address and base address of basic LUT register
    DISPLAY_REG_BASE = 0x1000
    LUT0EWHR = (DISPLAY_REG_BASE + 0x00)
    LUT0XYR = (DISPLAY_REG_BASE + 0x40)
    LUT0BADDR = (DISPLAY_REG_BASE + 0x80)
    LUT0MFN = (DISPLAY_REG_BASE + 0xC0)
    LUT01AF = (DISPLAY_REG_BASE + 0x114)

    # update parameter setting register
    UP0SR = (DISPLAY_REG_BASE + 0x134)
    UP1SR = (DISPLAY_REG_BASE + 0x138)
    LUT0ABFRV = (DISPLAY_REG_BASE + 0x13C)
    UPBBADDR = (DISPLAY_REG_BASE + 0x17C)
    LUT0IMXY = (DISPLAY_REG_BASE + 0x180)
    LUTAFSR = (DISPLAY_REG_BASE + 0x224)
    BGVR = (DISPLAY_REG_BASE + 0x250)

    # system registers
    SYS_REG_BASE = 0x0000
    I80CPCR = (SYS_REG_BASE + 0x04)
    MCSR_BASE_ADDR = 0x0200
    MCSR = (MCSR_BASE_ADDR + 0x0000)
    LISAR = (MCSR_BASE_ADDR + 0x0008)

    CS = 8
    HRDY = 24
    RESET = 17
    VCOM = 1500


    def __init__(self):
        print("init")
        # initialize gpio
        GPIO.setup()
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)


    def lcdWaitForReady(self):
        print("hoge")

