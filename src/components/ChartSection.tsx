
import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, BarChart, Bar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar, AreaChart, Area, ResponsiveContainer } from 'recharts';
import { generateRandomData } from '../utils/dataGenerator';

interface ChartSectionProps {
  chartTypes: {
    temperature: string;
    humidity: string;
    pressure: string;
    vibration: string;
  };
  isLiveData: boolean;
}

const ChartSection = ({ chartTypes = { temperature: 'line', humidity: 'bar', pressure: 'radar', vibration: 'area' }, isLiveData = false }: Partial<ChartSectionProps> = {}) => {
  const [data, setData] = useState(generateRandomData());

  useEffect(() => {
    if (isLiveData) {
      const interval = setInterval(() => {
        setData(generateRandomData());
      }, 3000); // Update every 3 seconds for live data
      return () => clearInterval(interval);
    }
  }, [isLiveData]);

  const renderChart = (type: string, chartData: any[], title: string, color: string) => {
    const chartProps = {
      height: 250,
      data: chartData
    };

    switch (type) {
      case 'line':
        return (
          <LineChart {...chartProps}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="value" stroke={color} strokeWidth={2} />
          </LineChart>
        );
      case 'bar':
        return (
          <BarChart {...chartProps}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="value" fill={color} />
          </BarChart>
        );
      case 'area':
        return (
          <AreaChart {...chartProps}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" />
            <YAxis />
            <Tooltip />
            <Area type="monotone" dataKey="value" stroke={color} fill={color} fillOpacity={0.6} />
          </AreaChart>
        );
      case 'radar':
        return (
          <RadarChart {...chartProps}>
            <PolarGrid />
            <PolarAngleAxis dataKey="subject" />
            <PolarRadiusAxis />
            <Radar name={title} dataKey="value" stroke={color} fill={color} fillOpacity={0.6} />
          </RadarChart>
        );
      default:
        return (
          <LineChart {...chartProps}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="value" stroke={color} strokeWidth={2} />
          </LineChart>
        );
    }
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
      {/* Temperature Chart */}
      <div className="bg-white rounded-lg shadow p-8 border border-gray-200">
        <h3 className="text-xl font-semibold text-gray-900 mb-6">Temperature</h3>
        <ResponsiveContainer width="100%" height={250}>
          {renderChart(chartTypes.temperature, data.temperature, 'Temperature', '#3B82F6')}
        </ResponsiveContainer>
      </div>

      {/* Humidity Chart */}
      <div className="bg-white rounded-lg shadow p-8 border border-gray-200">
        <h3 className="text-xl font-semibold text-gray-900 mb-6">Humidity</h3>
        <ResponsiveContainer width="100%" height={250}>
          {renderChart(chartTypes.humidity, data.humidity, 'Humidity', '#10B981')}
        </ResponsiveContainer>
      </div>

      {/* Pressure Chart */}
      <div className="bg-white rounded-lg shadow p-8 border border-gray-200">
        <h3 className="text-xl font-semibold text-gray-900 mb-6">Pressure</h3>
        <ResponsiveContainer width="100%" height={250}>
          {renderChart(chartTypes.pressure, data.pressure, 'Pressure', '#F59E0B')}
        </ResponsiveContainer>
      </div>

      {/* Vibration Chart */}
      <div className="bg-white rounded-lg shadow p-8 border border-gray-200">
        <h3 className="text-xl font-semibold text-gray-900 mb-6">Vibration</h3>
        <ResponsiveContainer width="100%" height={250}>
          {renderChart(chartTypes.vibration, data.energy, 'Vibration', '#8B5CF6')}
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default ChartSection;
