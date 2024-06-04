#!/usr/bin/python

from src.telegram_bot import enviar_mensaje
from src.utils import *
import sys
import os

act_dir = os.path.dirname(os.path.abspath(__file__))
proyect_dir = os.path.join(act_dir, 'src')
sys.path.append(proyect_dir)


if __name__ == "__main__":

    asyncio.run(enviar_mensaje('Etiquetado_AXA'))

    load(transform(os.path.join(act_dir, 'sql', 'df_extend_inb_172.70.7.32.sql'),
                   df_recording_log_30, 15, 'inbound'))

    load(transform(os.path.join(act_dir, 'sql', 'df_extend_inb_172.70.7.41.sql'),
                   df_recording_log_40, 15, 'inbound'))

    load(transform(os.path.join(act_dir, 'sql', 'df_extend_out_172.70.7.20.sql'),
                   df_recording_log_30, 45, 'outbound'))

    load(transform(os.path.join(act_dir, 'sql', 'df_extend_out_172.70.7.32.sql'),
                   df_recording_log_30, 45, 'outbound'))

    asyncio.run(enviar_mensaje("____________________________________"))
