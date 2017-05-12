# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:29:36 2017

@author: Calil
"""

from sharc.support.named_tuples import AntennaPar

class ParametersAntennaImt(object):
    """
    Defines parameters for antenna array.
    """
    
    __instance = None
    
    def __new__(cls):
        """
        This is the Singleton Pattern to ensure that this class will have only
        one instance
        """
        if ParametersAntennaImt.__instance is None:
            ParametersAntennaImt.__instance = object.__new__(cls)
        return ParametersAntennaImt.__instance
    
    ###########################################################################
    # BS transmit antenna type. Possible values are "OMNI", "BEAMFORMING"
    bs_tx_antenna_type = "OMNI"
    
    ###########################################################################
    # BS receive antenna type. Possible values are "OMNI", "BEAMFORMING"
    bs_rx_antenna_type = "OMNI"
    
    ###########################################################################
    # UE transmit antenna type. Possible values are "OMNI", "BEAMFORMING"
    ue_tx_antenna_type = "OMNI"
    
    ###########################################################################
    # UE receive antenna type. Possible values are "OMNI", "BEAMFORMING"
    ue_rx_antenna_type = "OMNI"
    
    ###########################################################################
    # OMNIDIRECTIONAL ANTENNA PARAMETERS
    ###########################################################################
    # Base station transmit antenna gain [dBi]
    bs_tx_omni_antenna_gain = 0

    ###########################################################################
    # Base station receive antenna gain [dBi]
    bs_rx_omni_antenna_gain = 0

    ###########################################################################
    # UE transmit antenna gain [dBi]
    ue_tx_omni_antenna_gain = 0

    ###########################################################################
    # UE receive antenna gain [dBi]
    ue_rx_omni_antenna_gain = 0
    
    ###########################################################################
    # BEAMFORMING PARAMETERS
    ###########################################################################
    # BS sector azimuth angle [degrees]
    bs_tx_azimuth = [60, 180, 300]
    
    ###########################################################################
    # BS sector elevation angle [degrees]
    bs_tx_elevation = -10
    
    ###########################################################################
    # Base station maximum transmit element gain [dBi]
    bs_tx_element_max_g = 5
    
    ###########################################################################
    # Base station horizontal 3dB beamwidth of single transmit element [degrees]
    bs_tx_element_phi_3db = 80
    
    ###########################################################################
    # Base station vertical 3dB beamwidth of single transmit element [degrees]
    bs_tx_element_theta_3db = 65
    
    ###########################################################################
    # Base station front to back ratio of single transmit element [dB]
    bs_tx_element_am = 30
    
    ###########################################################################
    # Base station transmit element vertical sidelobe attenuation [dB]
    bs_tx_element_sla_v = 30
    
    ###########################################################################
    # Base station number of rows in transmit array
    bs_tx_n_rows = 16
    
    ###########################################################################
    # Base station number of columns in transmit array
    bs_tx_n_columns = 16
    
    ###########################################################################
    # Base station array horizontal transmit element spacing (d/lambda)
    bs_tx_element_horiz_spacing = 0.5
    
    ###########################################################################
    # Base station array vertical transmit element spacing (d/lambda)
    bs_tx_element_vert_spacing = 0.5
    
    ###########################################################################
    # BS sector azimuth angle [degrees]
    bs_rx_azimuth = [60, 180, 300]
    
    ###########################################################################
    # BS sector elevation angle [degrees]
    bs_rx_elevation = -10
    
    ###########################################################################
    # Base station maximum receive element gain [dBi]
    bs_rx_element_max_g = 5
    
    ###########################################################################
    # Base station horizontal 3dB beamwidth of single receive element [degrees]
    bs_rx_element_phi_3db = 80
    
    ###########################################################################
    # Base station vertical 3dB beamwidth of single receive element [degrees]
    bs_rx_element_theta_3db = 65
    
    ###########################################################################
    # Base station front to back ratio of single receive element [dB]
    bs_rx_element_am = 30
    
    ###########################################################################
    # Base station receive element vertical sidelobe attenuation [dB]
    bs_rx_element_sla_v = 30
    
    ###########################################################################
    # Base station number of rows in receive array
    bs_rx_n_rows = 16
    
    ###########################################################################
    # Base station number of columns in receive array
    bs_rx_n_columns = 16
    
    ###########################################################################
    # Base station array horizontal receive element spacing (d/lambda)
    bs_rx_element_horiz_spacing = 0.5
    
    ###########################################################################
    # Base station array vertical receive element spacing (d/lambda)
    bs_rx_element_vert_spacing = 0.5
    
    ###########################################################################
    # UE pointing type. Possible values are "FIXED" and "RANDOM".
    ue_tx_pointing = "FIXED"
    
    ###########################################################################
    # UEs azimuth angle, if fixed [degrees]
    ue_tx_azimuth = 0
    
    ###########################################################################
    # UEs elevation angle, if fixed [degrees]
    ue_tx_elevation = 0
    
    ###########################################################################
    # UE maximum transmit element gain [dBi]
    ue_tx_element_max_g = 5
    
    ###########################################################################
    # UE horizontal 3dB beamwidth of single transmit element [degrees]
    ue_tx_element_phi_3db = 80
    
    ###########################################################################
    # UE vertical 3dB beamwidth of single transmit element [degrees]
    ue_tx_element_theta_3db = 65
    
    ###########################################################################
    # UE front to back ratio of single transmit element [dB]
    ue_tx_element_am = 30
    
    ###########################################################################
    # UE transmit element vertical sidelobe attenuation [dB]
    ue_tx_element_sla_v = 30
    
    ###########################################################################
    # UE number of rows in transmit array
    ue_tx_n_rows = 4
    
    ###########################################################################
    # UE number of columns in transmit array
    ue_tx_n_columns = 2
    
    ###########################################################################
    # UE array horizontal transmit element spacing (d/lambda)
    ue_tx_element_horiz_spacing = 0.5
    
    ###########################################################################
    # UE array vertical transmit element spacing (d/lambda)
    ue_tx_element_vert_spacing = 0.5
    
    ###########################################################################
    # UE pointing type. Possible values are "FIXED" and "RANDOM".
    ue_rx_pointing = "FIXED"
    
    ###########################################################################
    # UEs azimuth angle, if fixed [degrees]
    ue_rx_azimuth = 0
    
    ###########################################################################
    # UEs elevation angle, if fixed [degrees]
    ue_rx_elevation = 0
    
    ###########################################################################
    # UE maximum receive element gain [dBi]
    ue_rx_element_max_g = 5
    
    ###########################################################################
    # UE horizontal 3dB beamwidth of single receive element [degrees]
    ue_rx_element_phi_3db = 80
    
    ###########################################################################
    # UE vertical 3dB beamwidth of single receive element [degrees]
    ue_rx_element_theta_3db = 65
    
    ###########################################################################
    # UE front to back ratio of single receive element [dB]
    ue_rx_element_am = 30
    
    ###########################################################################
    # UE receive element vertical sidelobe attenuation [dB]
    ue_rx_element_sla_v = 30
    
    ###########################################################################
    # UE number of rows in receive array
    ue_rx_n_rows = 4
    
    ###########################################################################
    # UE number of columns in receive array
    ue_rx_n_columns = 2
    
    ###########################################################################
    # UE array horizontal receive element spacing (d/lambda)
    ue_rx_element_horiz_spacing = 0.5
    
    ###########################################################################
    # UE array vertical receive element spacing (d/lambda)
    ue_rx_element_vert_spacing = 0.5
    
    ###########################################################################
    # Named tuples which contain antenna types
    
    def get_antenna_parameters(self,sta_type: str, txrx: str)-> AntennaPar:
        if sta_type == "BS":
            if txrx == "TX":
                tpl = AntennaPar(self.bs_tx_element_max_g,\
                                       self.bs_tx_element_phi_3db,\
                                       self.bs_tx_element_theta_3db,\
                                       self.bs_tx_element_am,\
                                       self.bs_tx_element_sla_v,\
                                       self.bs_tx_n_rows,\
                                       self.bs_tx_n_columns,\
                                       self.bs_tx_element_horiz_spacing,\
                                       self.bs_tx_element_vert_spacing)
            elif txrx == "RX":
                tpl = AntennaPar(self.bs_rx_element_max_g,\
                                       self.bs_rx_element_phi_3db,\
                                       self.bs_rx_element_theta_3db,\
                                       self.bs_rx_element_am,\
                                       self.bs_rx_element_sla_v,\
                                       self.bs_rx_n_rows,\
                                       self.bs_rx_n_columns,\
                                       self.bs_rx_element_horiz_spacing,\
                                       self.bs_rx_element_vert_spacing)
        elif sta_type == "UE":
            if txrx == "TX":
                tpl = AntennaPar(self.ue_tx_element_max_g,\
                                       self.ue_tx_element_phi_3db,\
                                       self.ue_tx_element_theta_3db,\
                                       self.ue_tx_element_am,\
                                       self.ue_tx_element_sla_v,\
                                       self.ue_tx_n_rows,\
                                       self.ue_tx_n_columns,\
                                       self.ue_tx_element_horiz_spacing,\
                                       self.ue_tx_element_vert_spacing)
            elif txrx == "RX":
                tpl = AntennaPar(self.ue_rx_element_max_g,\
                                       self.ue_rx_element_phi_3db,\
                                       self.ue_rx_element_theta_3db,\
                                       self.ue_rx_element_am,\
                                       self.ue_rx_element_sla_v,\
                                       self.ue_rx_n_rows,\
                                       self.ue_rx_n_columns,\
                                       self.ue_rx_element_horiz_spacing,\
                                       self.ue_rx_element_vert_spacing)
                
        return tpl