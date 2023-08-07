from sysdata.config.configdata import Config
from systems.provided.futures_chapter15.basesystem import futures_system

my_config=Config("private.private_config.yaml")
system=futures_system(config=my_config)
system.rules.get_raw_forecast("EDOLLAR", "sma7_14")
system.accounts.pandl_for_instrument_forecast("EDOLLAR", "sma7_14").sharpe() ## Sharpe for a specific trading rule variation
print('a')
