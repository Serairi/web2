
import React from 'react';
import { Button } from '@/components/ui/button';

interface RightPanelProps {
  chartTypes: {
    temperature: string;
    humidity: string;
    pressure: string;
    vibration: string;
  };
  onChartTypeChange: (metric: string, type: string) => void;
}

const RightPanel = ({ 
  chartTypes = { temperature: 'line', humidity: 'bar', pressure: 'radar', vibration: 'area' },
  onChartTypeChange = () => {}
}: Partial<RightPanelProps> = {}) => {
  
  const chartTypeOptions = [
    { value: 'line', label: 'Line chart' },
    { value: 'bar', label: 'Bar chart' },
    { value: 'area', label: 'Area chart' },
    { value: 'radar', label: 'Radar chart' }
  ];

  const handleExportCSV = () => {
    console.log('Exporting CSV...');
    // Add CSV export logic here
  };

  const handleExportPDF = () => {
    console.log('Exporting PDF...');
    // Add PDF export logic here
  };

  return (
    <div className="w-80 bg-white border-l border-gray-200 p-6">
      <div className="space-y-8">
        {/* Chart Settings */}
        <div>
          <h3 className="text-xl font-semibold text-gray-900 mb-6">Chart Settings</h3>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">Temperature</label>
              <select 
                className="w-full border border-gray-300 rounded px-3 py-2 text-sm bg-white"
                value={chartTypes.temperature}
                onChange={(e) => onChartTypeChange('temperature', e.target.value)}
              >
                {chartTypeOptions.map(option => (
                  <option key={option.value} value={option.value}>{option.label}</option>
                ))}
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">Humidity</label>
              <select 
                className="w-full border border-gray-300 rounded px-3 py-2 text-sm bg-white"
                value={chartTypes.humidity}
                onChange={(e) => onChartTypeChange('humidity', e.target.value)}
              >
                {chartTypeOptions.map(option => (
                  <option key={option.value} value={option.value}>{option.label}</option>
                ))}
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">Pressure</label>
              <select 
                className="w-full border border-gray-300 rounded px-3 py-2 text-sm bg-white"
                value={chartTypes.pressure}
                onChange={(e) => onChartTypeChange('pressure', e.target.value)}
              >
                {chartTypeOptions.map(option => (
                  <option key={option.value} value={option.value}>{option.label}</option>
                ))}
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">Vibration</label>
              <select 
                className="w-full border border-gray-300 rounded px-3 py-2 text-sm bg-white"
                value={chartTypes.vibration}
                onChange={(e) => onChartTypeChange('vibration', e.target.value)}
              >
                {chartTypeOptions.map(option => (
                  <option key={option.value} value={option.value}>{option.label}</option>
                ))}
              </select>
            </div>
          </div>
        </div>

        {/* Export Data */}
        <div>
          <h3 className="text-xl font-semibold text-gray-900 mb-6">Export Data</h3>
          <div className="space-y-3">
            <Button 
              variant="outline" 
              className="w-full text-base py-3"
              onClick={handleExportCSV}
            >
              Download CSV
            </Button>
            <Button 
              variant="outline" 
              className="w-full text-base py-3"
              onClick={handleExportPDF}
            >
              Download PDF
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RightPanel;
