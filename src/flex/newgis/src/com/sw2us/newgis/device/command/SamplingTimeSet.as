
//等时连续回传设置
package com.sw2us.newgis.device.command
{
	public class SamplingTimeSet extends CommandBase
	{
		public function SamplingTimeSet()
		{
			super(AOCTRL_CMD_SAMPLING_TIMESET);
		}
	}
}